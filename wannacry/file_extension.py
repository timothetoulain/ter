#check for suspicious file extensions

from pathlib import Path
import time

#file extensions to check, .txt was added as an example
types=('*.txt','@Please_Read_Me@.txt','*.wnry','*.wcry','*.wncry','*.wncryt')
files_grabbed=[]

while True:
	for files in types:
		#change path for windows
		files_grabbed.extend(Path('/home/tim/test').rglob(files))
		if len(files_grabbed)!=0:
			print(files_grabbed[0])
			del files_grabbed[0]

	print("\n[*] restarting file checking")
	time.sleep(1)

