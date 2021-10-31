import sys

def hash10(demoStr):
    hashVal = hash(demoStr)
    if(hashVal <= 0 or hashVal >= 1024):
        compressedVal = (hashVal % 1024)
    return compressedVal

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		print("Please enter filename to be hashed as an argument.")
		print("python hashfile.py <File_to_be_hashed>")
		sys.exit()
	else:
		f = open(sys.argv[1], "r")
		for x in f:
		  print(hash10(x))