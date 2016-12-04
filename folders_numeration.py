import os, sys 

# reading directories in the list
root  = "/home/username/Dropbox/folder/folder"
dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]

print(dirlist[0], len(dirlist), dirlist[0][0:2])

# checking if directory name starts with a number
for item in dirlist:
	if item[2] == ".":
		old_item = root + "/" + item
		new_item = root + "/0"+str(item)
		os.rename(old_item, new_item)
		print(new_item)
