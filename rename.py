import os

def rename_files():
	# get file names from a folder
	file_list = os.listdir(r"./prank")

	# print path
	saved_path = os.getcwd()
	print "current path:{}".format(saved_path)
	# Change the path
	os.chdir(r"./prank")
	saved_path = os.getcwd()
	print "current path:{}".format(saved_path)
	# for each file, rename filename
	for file_name in file_list:
		print("Old Name - "+ file_name)
		print("Old Name - "+ file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()