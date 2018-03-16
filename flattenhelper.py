#FlattenAllVideosToDestination.py by Ryan Graham
import os
import shutil
import sys

class FlattenHelper:
	#source = '//cerberus/download/'
	#destination = '//cerberus/download/'
	print (len(sys.argv))
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("You must provide source and destination paths.")
		print("example: py flattenhelper.py \"/test/\" \"./test/\"")
		sys.exit()

	source = sys.argv[1]
	destination = sys.argv[2]

	extensions = set(["mp4","avi","mkv","mov","mpg","wmv"])
	notMigratedList = "notMigrated.csv"
	migratedList = "migrated.csv"
	numberOfMoviesMigrated = 0
	numberOfFilesFound = 0

	def flattenTheVideos(self):
		with open(FlattenHelper.notMigratedList, 'w') as notMigratedFileList:	
			with open(FlattenHelper.migratedList, 'w') as migratedFileList:	
				print(FlattenHelper.source)
				# traverse root directory, and list directories as dirs and files as files
				for root, dirs, files in os.walk(FlattenHelper.source):
					path = root.split(os.sep)
					for file in files:
						FlattenHelper.numberOfFilesFound += 1
						moveFrom = os.path.join(root,file)
						moveTo = os.path.join(FlattenHelper.destination,file)
						fileExtension = file.rsplit('.',1)[1]
						if (moveFrom != moveTo):
							if (fileExtension in FlattenHelper.extensions):
								print("moving " + moveFrom + " to " + moveTo)
								migratedFileList.write(moveFrom + "," + str(moveFrom).rsplit('.',1)[1]+"\n")
								shutil.move(moveFrom, moveTo)
								FlattenHelper.numberOfMoviesMigrated += 1
							else:
								notMigratedFileList.write(moveFrom + "," + str(moveFrom).rsplit('.',1)[1]+"\n")
								
		print("Completed migrating.\n" + "Migrated " + str(FlattenHelper.numberOfMoviesMigrated) + " of " + str(FlattenHelper.numberOfFilesFound) + " files")
		
flattenHelper = FlattenHelper()
flattenHelper.flattenTheVideos()