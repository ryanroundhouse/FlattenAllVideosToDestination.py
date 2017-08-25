#FlattenAllVideosToDestination.py by Ryan Graham
import os
import shutil

source = '//cerberus/download/'
destination = '//cerberus/download/'

extensions = set(["mp4","avi","mkv","mov","mpg","wmv"])
notMigratedList = "notMigrated.csv"
migratedList = "migrated.csv"
numberOfMoviesMigrated = 0
numberOfFilesFound = 0

with open(notMigratedList, 'w') as notMigratedFileList:	
	with open(migratedList, 'w') as migratedFileList:	
		# traverse root directory, and list directories as dirs and files as files
		for root, dirs, files in os.walk(source):
			path = root.split(os.sep)
			for file in files:
				numberOfFilesFound += 1
				moveFrom = os.path.join(root,file)
				moveTo = os.path.join(source,file)
				fileExtension = file.rsplit('.',1)[1]
				if (moveFrom != moveTo):
					if (fileExtension in extensions):
						print("moving " + moveFrom + " to " + moveTo)
						migratedFileList.write(moveFrom + "," + str(moveFrom).rsplit('.',1)[1]+"\n")
						shutil.move(moveFrom, moveTo)
						numberOfMoviesMigrated += 1
					else:
						notMigratedFileList.write(moveFrom + "," + str(moveFrom).rsplit('.',1)[1]+"\n")
						
print("completed migrating.")
print("migrated " + str(numberOfMoviesMigrated) + " of " + str(numberOfFilesFound) + " files")