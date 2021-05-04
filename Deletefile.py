# code to delete entire data along with file
import os

file = input("ENTER YOUR FILE NAME:-")
# check if file exists
if os.path.exists(file):
	os.remove(file)

	# Print the statement once
	# the file is deleted
	print("File deleted !")

else:

	# Print if file is not present
	print("File doesnot exist !")
