import sys

def hash10(demoStr):
    hashVal = hash(demoStr)
    if(hashVal <= 0 or hashVal >= 1024):
        compressedVal = (hashVal % 1024)
    return compressedVal

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		print("Please enter string to be hashed as an argument.")
		print("python hash10.py <String_to_be_hashed>")
		sys.exit()
	else:
		demoStr = " ".join(sys.argv[1:])
		compressedVal = hash10(demoStr)
		print ("Compressed Hash value for given string is: ", compressedVal)