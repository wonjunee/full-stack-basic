import os

def rename_files():
	# get file names from a folder
	file_list = os.listdir(r"./prank")
	print(file_list)

rename_files()