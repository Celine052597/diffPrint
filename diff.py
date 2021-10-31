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


# Open File in Read Mode
file_1 = open('file1.txt', 'r')
file_2 = open('file2.txt', 'r')

print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')

file_1_line = file_1.readline()
file_2_line = file_2.readline()

# Use as a COunter
line_no = 1

print()

with open('file1.txt') as file1:
	with open('file2.txt') as file2:
		same = set(file1).intersection(file2)

print("Common Lines in Both Files")

for line in same:
	print(line, end='')

print('\n')
print("Difference Lines in Both Files")
while file_1_line != '' or file_2_line != '':

	# Removing whitespaces
	file_1_line = file_1_line.rstrip()
	file_2_line = file_2_line.rstrip()

	# Compare the lines from both file
	if file_1_line != file_2_line:
		
		# otherwise output the line on file1 and use @ sign
		if file_1_line == '':
			print("@", "Line-%d" % line_no, file_1_line)
		else:
			print("@-", "Line-%d" % line_no, file_1_line)
			
		# otherwise output the line on file2 and use # sign
		if file_2_line == '':
			print("#", "Line-%d" % line_no, file_2_line)
		else:
			print("#+", "Line-%d" % line_no, file_2_line)

		# Print a empty line
		print()

	# Read the next line from the file
	file_1_line = file_1.readline()
	file_2_line = file_2.readline()

	line_no += 1

file_1.close()
file_2.close()
