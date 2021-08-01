# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 04:11:51 2021

@author: AsteriskAmpersand
"""
import crccheck
import subprocess
import os
import sys
from pathlib import Path
from Cryptodome.Cipher import Blowfish
from Cryptodome.Hash import SHA1

from EncryptionKeys import keys

def nullOutput(*args,**kwargs):
    return

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
def endianness_reversal(data):
    return b''.join(map(lambda x: x[::-1],chunks(data, 4)))

def CapcomDecrypt(file, key ):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    return bytearray(endianness_reversal(cipher.decrypt(endianness_reversal(file))))

def CapcomEncrypt(file, key ):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    return endianness_reversal(cipher.encrypt(endianness_reversal(file)))
        
def replaceData(inFile, outFile, value):
    w = inFile.open("rb").read()#CapcomDecrypt()
    #w[10:14] = struct.pack("I",value)
    with outFile.open("wb") as outf:
        outf.write(w)#CapcomEncrypt()
    return

def crc32(key):
    return crccheck.crc.CrcJamcrc().calc(key).to_bytes(4,"little")

def sha1(data):
    h = SHA1.new()
    h.update(data)
    return endianness_reversal(h.digest())

hexToBin = lambda keycandidate: bytes(map(lambda x: int(x,16),keycandidate.split(" ")))
decToBin = lambda keycandidate: bytes(map(lambda x: int(x,10),keycandidate.split(" ")))

HEADER = 0x30
SHASTART = 0x40
STEAMIDLOC = 8407304
    
def buildHeader(dBody,pckey):
    preamble = hexToBin("01 00 00 00 00 00 00 00 18 00 00 00")
    key = crc32(pckey)  
    mid = hexToBin("70 80 80 00")
    epilogue = hexToBin("00 00 00 00 00 00 00 00")    
    sha = sha1(dBody[SHASTART:])
    return preamble+sha+mid+key+epilogue

def replaceHeader(dBody,pckey):    
    return buildHeader(dBody,pckey)+dBody[HEADER:]

def getSteamKey(steamId64):
    #exe = sys.executable
    pq = subprocess.Popen(["AndoStories2Tool.exe",str(steamId64)],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    result = pq.communicate()[0]
    key,steam32id = result.split(b"\n")
    return key[:-2],int(steam32id)

def insertID(dbody,steamId32):
    return dbody[:STEAMIDLOC]+steamId32.to_bytes(4,"little")+dbody[STEAMIDLOC+4:]

def steamTransfer(dBody,pckey,steamid32):
    dBody = insertID(dBody,steamid32)
    dBody = replaceHeader(dBody,pckey)
    return dBody

def dataSwitchToPC(switchdata,pckey,steamId32):    
    epilogue = hexToBin("00 00 00 00 00 00 00 00")
    skeleton = switchdata[:0xC] + b"\x00"*HEADER + switchdata[0xC:] + epilogue
    return steamTransfer(skeleton,pckey,steamId32)

def dataPCToSwitch(dPcdata):
    insertID(dPcdata,0)
    return dPcdata[:0xC]+dPcdata[0xC+HEADER:-8]

def fileSwitchToPC(switchfilepath,steamId64,pcfilepath):
    with open(switchfilepath,"rb") as inf:
        dSwitch = inf.read()
    pckey,steamId32 = getSteamKey(steamId64)
    dBody = dataSwitchToPC(dSwitch,pckey,steamId32)    
    eBody = CapcomEncrypt(dBody,pckey)
    with open(pcfilepath,"wb") as outf:
        outf.write(eBody)

def tryKeys(eBody):
    teststr = eBody[-8:]
    for key in keys:
        test = CapcomDecrypt(teststr,key[:-1])
        if sum(test) == 0:
            return key[:-1]
    else:        
        raise ValueError("Could not find encryption key")        

def filePCtoPC(pcfilepath,steamId64,pcfilepathout):
    with open(pcfilepath,"rb") as inf:
        eBody = inf.read()
    inkey = tryKeys(eBody)
    pckey,steamId32 = getSteamKey(steamId64)
    dBody = CapcomDecrypt(eBody,inkey)
    dOut = steamTransfer(dBody,pckey,steamId32)
    eOut = CapcomEncrypt(dOut,pckey)
    with open(pcfilepathout,"wb") as outf:
        outf.write(eOut)
        
def filePCtoSwitch(pcfilepath,switchfilepathout,output = nullOutput):
    output("Converting")
    output("    from PC Save File:%s"%(pcfilepath))
    output("    to  NSW Save File:%s"%(switchfilepathout))
    with open(pcfilepath,"rb") as inf:
        eBody = inf.read()
    if len(eBody) != 8421552:
        output("%s is not a PC Save File"%(pcfilepath))
        return
        raise ValueError("Not a PC MHS2 Save File")
    inkey = tryKeys(eBody)
    dBody = CapcomDecrypt(eBody,inkey)
    dOut = dataPCToSwitch(dBody)
    with open(switchfilepathout,"wb") as outf:
        outf.write(dOut)
    output("Completed Conversion")

def fileTransfer(filepath,steamId64,fileout,output = nullOutput):
    fsize = os.stat(filepath).st_size
    if fsize == 8421552:
        output("Converting")
        output("    from PC Save File:%s"%(filepath))
        output("    to   PC Save File:%s"%(fileout))
        filePCtoPC(filepath,steamId64,fileout)
    elif fsize == 8421496:
        output("Converting")
        output("    from NSW Save File:%s"%(filepath))
        output("    to    PC Save File:%s"%(fileout))
        fileSwitchToPC(filepath,steamId64,fileout)
    else:
        raise ValueError("Not a MHS2 Save File")
    output("Completed Conversion")

def decryptPC(pcfilepath,pcfilepathout,output = nullOutput):
    with open(pcfilepath,"rb") as inf:
        eBody = inf.read()
    if len(eBody) != 8421552:
        output("%s is not a PC Save File"%(pcfilepath))
        return
        raise ValueError("Not a PC MHS2 Save File")
    pckey = tryKeys(eBody)
    output("Decryption Key %s"%pckey)
    dBody = CapcomDecrypt(eBody,pckey)
    with open(pcfilepathout,"wb") as outf:
        outf.write(dBody)
    output("Completed Decryption")
        
def encryptPC(pcfilepath,steamId64,pcfilepathout,output = nullOutput):
    with open(pcfilepath,"rb") as inf:
        dBody = inf.read()
    if len(dBody) != 8421552:
        output("%s is not a PC Save File"%(pcfilepath))
        return
        raise ValueError("Not a PC MHS2 Save File")
    pckey,steamId32 = getSteamKey(steamId64)
    output("Decryption Key [%s]"%pckey.decode())
    output("Partial ID %X"%steamId32)
    dOut = steamTransfer(dBody,pckey,steamId32)
    eBody = CapcomEncrypt(dOut,pckey)
    with open(pcfilepathout,"wb") as outf:
        outf.write(eBody)
    output("Completed Encryption")


SKIN_TONE_PRESETS = [
    [0x87, 0x5D, 0x46, 0x00], # Converts to [0x87, 0x41, 0x26, 0x00],
    [0xB8, 0x86, 0x65, 0x00], # Converts to [0xB6, 0x6A, 0x37, 0x00],
    [0xDE, 0xAB, 0x8E, 0x00], # Converts to [0xDE, 0x88, 0x4D, 0x00],
    [0xEA, 0xC8, 0xA6, 0x00], # Converts to [0xEA, 0x9F, 0x5A, 0x00],
    [0xF9, 0xE9, 0xD2, 0x00], # Converts to [0xF9, 0xB9, 0x72, 0x00],
    [0xFF, 0xFF, 0xFF, 0x00], # Converts to [0xFF, 0xCB, 0x8B, 0x00],
]

SKIN_TONE_OFFSET = 0x2D2B08
SKIN_TONE_OFFSET_2 = 0x8000E8
# Fixes the "Corrupt Data" multiplayer issue caused by non-preset skin tones
def fixSave(pcfilepath, pcfilepathout, steamId64, skinChoice, output = nullOutput):
    with open(pcfilepath,"rb") as inf:
        eBody = inf.read()
    if len(eBody) != 8421552:
        output("%s is not a PC Save File"%(pcfilepath))
        return

    # Decrypt
    pckey = tryKeys(eBody)
    output("Decryption Key %s"%pckey)
    dBody = CapcomDecrypt(eBody,pckey)

    # Patch skin tone to chosen present.
    choiceData = SKIN_TONE_PRESETS[skinChoice]
    dBody[SKIN_TONE_OFFSET:SKIN_TONE_OFFSET+4] = choiceData
    dBody[SKIN_TONE_OFFSET_2:SKIN_TONE_OFFSET_2+4] = choiceData
    output("Updated skin tone to: %s"%''.join(['%X'%x for x in choiceData]))

    # Encrypt
    pckey,steamId32 = getSteamKey(steamId64)
    output("Partial ID %X"%steamId32)
    dOut = steamTransfer(dBody,pckey,steamId32)
    eBody = CapcomEncrypt(dOut,pckey)
    try:
        with open(pcfilepathout,"wb") as outf:
            outf.write(eBody)
        output("Completed Encryption")
    except:
        output("Couldn't write to output file")

if __name__ in '__main__':
    import struct
    saveTarget = sys.argv[1]
    with open(saveTarget,"rb") as inf:
        magic = inf.read(4)
        inf.seek(STEAMIDLOC)
        steam32 = struct.unpack("i",inf.read(4))[0]
    if magic == b'\x1C\xCC\xE3\x5F':
        decryptPC(saveTarget,saveTarget)
    else:
        steamid = steam32+76561197960265728
        encryptPC(saveTarget,steamid,saveTarget)