# -*- coding: utf-8 -*-

import sys

"""Question A"""

def calculateHash(demoStr):
    hashVal = hash(demoStr)
    if(hashVal <= 0 or hashVal >= 1024):
        compressedVal = (hashVal % 1024)
    return compressedVal

"""Question B"""

if(len(sys.argv) < 3):
	print("Please enter filename to be hashed as an argument.")
	print("python diff.py <File_1> <File_2>")
	sys.exit()
else:
	filenames = []
	filenames.append(sys.argv[1])
	filenames.append(sys.argv[2])

	hashData = []
	for filename in filenames:
		with open("./data/"+filename, "r") as f:
			data = f.readlines()
			hashData.append([calculateHash(line.replace("\n","")) for line in data])
		f.close()

"""Question C"""

def diff(file1, file2):
  L = [[0 for x in range(len(file2)+1)] for x in range(len(file1)+1)]

  for i in range(len(file1)+1): 
    for j in range(len(file2)+1): 
      if i == 0 or j == 0: 
        L[i][j] = 0
      elif file1[i-1] == file2[j-1]: 
        L[i][j] = L[i-1][j-1] + 1
      else: 
        L[i][j] = max(L[i-1][j], L[i][j-1])

  index = L[len(file1)][len(file2)] 
  lcs = [""] * (index+1) 
  lcs[index] = ""

  i = len(file1)
  j = len(file2)
  while i > 0 and j > 0: 
      if file1[i-1] == file2[j-1]: 
        lcs[index-1] = file1[i-1] 
        i-=1
        j-=1
        index-=1

      elif L[i-1][j] > L[i][j-1]: 
        i-=1
      else: 
        j-=1
  fileOutput1 = [str(file1.index(item)+1) for item in lcs[:-1]]
  fileOutput2 = [str(file2.index(item)+1) for item in lcs[:-1]]

  return fileOutput1, fileOutput2

file1 = hashData[0]
file2 = hashData[1]

fileOutput1, fileOutput2 = diff(file1, file2)
print(" ".join(fileOutput1))
print(" ".join(fileOutput2))