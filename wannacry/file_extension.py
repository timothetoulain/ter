#check for suspicious file extensions
#we need to determine if the system is linux or windows though

from pathlib import Path
import time

#file extensions to check, .txt was added as an example
types=('*.txt','*.wnry','*.wcry','*.wncry','*.wncryt')
files_grabbed=[]

while True:
	for files in types:
		files_grabbed.extend(Path('/home/tim/test').rglob(files))
		if len(files_grabbed)!=0:

			files_print.append(files_grabbed[0])
			print(files_grabbed[0])
			del files_grabbed[0]

	print("\n[*] restarting file checking")
	time.sleep(1)

