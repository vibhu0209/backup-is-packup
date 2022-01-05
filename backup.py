import os
import shutil
import time


def main():

	foldersDeleted = 0
	filesDeleted = 0
	path = input("Enter The path to delete  ")
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for rootFolder, folders, files in os.walk(path):

			if seconds >= ageOfFile(rootFolder):

				removeFolder(rootFolder)
				foldersDeleted += 1 
				break

			else:

				for folder in folders:

					folder_path = os.path.join(rootFolder, folder)

					
					if seconds >= ageOfFile(folder_path):

						
						removeFolder(folder_path)
						foldersDeleted += 1 
				
				for file in files:

					file_path = os.path.join(rootFolder, file)

				
					if seconds >= ageOfFile(file_path):

						remove_file(file_path)
						filesDeleted += 1 

		else:

			if seconds >= ageOfFile(path):

				remove_file(path)
				filesDeleted += 1 
	else:

		print(f'"{path}" is not found')
		filesDeleted += 1 
	print(f"Total folders deleted: {foldersDeleted}")
	print(f"Total files deleted: {filesDeleted}")


def removeFolder(path):

	
	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		
		print(f"Unable to delete the "+path)



def remove_file(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the "+path)


def ageOfFile(path):

	ctime = os.stat(path).st_ctime

	return ctime


if '_name_' == '_main_':
	main()