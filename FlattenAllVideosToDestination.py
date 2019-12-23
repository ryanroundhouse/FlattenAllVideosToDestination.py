#FlattenAllVideosToDestination.py by Ryan Graham
import os
import shutil
import sys
import FlattenUtils
import ntpath

#source = '//cerberus/download/'
#destination = '//cerberus/download/'
if len(sys.argv) < 3 or len(sys.argv) > 3:
	print("You must provide source and destination paths.")
	print("example: py FlattenAllVideosToDestination.py \"/sourceDir/\" \"/destinationDir/\"")
	sys.exit(0)

source = sys.argv[1]
destination = sys.argv[2]

extensions = [".mp4",".avi",".mkv",".mov",".mpg",".wmv"]

numberOfVideosMigrated = 0
migrationList = FlattenUtils.getFilesToMigrate(source, extensions)
for fileSource in migrationList:
	head, tail = ntpath.split(fileSource)
	fileDestination = os.path.join(destination, tail)
	print("moving " + fileSource + " to " + fileDestination)
	shutil.move(fileSource, fileDestination)
	numberOfVideosMigrated += 1

print("moved " + str(numberOfVideosMigrated) + " files.")