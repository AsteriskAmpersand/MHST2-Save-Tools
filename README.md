# SaveTools
 MHS2 Save file editing tools. Transfers save files between players, switch and pc version, encrypts and decrypts.
 
## Credits
 Written by AsteriskAmpersand.  
 Based on research taken together with Andoryuuta to reverse engineer the save encryption.  
 Thanks to AkantoreX, Phemeto, ShinSeiKen and TheChief for their save files which were used for analysis and testing.  
 Thanks to Phemeto with help with testing the finished application.
 
## Dependencies
 Uses a compiled version of Andoryuuta MHS2SaveKeygen Project
 https://github.com/Andoryuuta/MHS2SaveKeygen

## Usage
There's one file that isn't yet covered, which is the mhr_sys.sav.  
This file controls which slots are active. Because of how encrypt works it's not meant to be used on this file. This means you cannot "add" slots. Simply save on a slot if you want to put something on it. If you have no slots you'll have to progress to the first screen where you have control and save at your house.

The 3 use cases for the tool are:
### Transfer PC Save to someone else
 - In: PC
 - Out: PC
 - Steam Id: Recipient Steam Id
 - Convert to Switch: No
 - Button: Convert

### Import Switch Save
 - In: NSW
 - Out: PC
 - Steam Id: Your Steam Id
 - Convert to Switch: No
 - Button: Convert

### Export PC Save to Switch
 - In: PC
 - Out: NSW
 - Steam Id: Not Needed/Won't be used
 - Convert to Switch: Yes
 - Button: Convert
