#FlattenAllVideosToDestination.py by Ryan Graham
import os
import shutil
import sys
import FlattenUtils
import EmailSummary
import ntpath
import datetime
import re

#source = '//cerberus/download/'
#videoDirectory = '//cerberus/video/Series/'
#movieDirectory = '//cerberus/video/Movies/'

if len(sys.argv) < 4 or len(sys.argv) > 4:
	print("You must provide source and destination paths.")
	print("example: py FlattenAllVideosToDestination.py \"/sourceDir/\" \"/seriesDirectory/\" \"/moviesDirectory\"")
	sys.exit(0)

source = sys.argv[1]
videoDirectory = sys.argv[2]
movieDirectory = sys.argv[3]

# File types to move
extensions = [".mp4",".avi",".mkv",".mov",".mpg",".wmv"]

# Big Summary
movieList = [""]

# Small Summary
seriesList = [""]

print("started run on " + str(datetime.datetime.now()))
numberOfVideosMigrated = 0
folderList = FlattenUtils.getFoldersWithVideoFiles(source, extensions)
migrationList = FlattenUtils.getFilesToMigrate(source, extensions)
for fileSource in migrationList:
	head, tail = ntpath.split(fileSource)
	fileSize = os.path.getsize(str(fileSource))
	fileDestination = os.path.join(source, tail)
	if re.match(r'[sS][0-9]{2}[eE][0-9]{2}', tail):
		fileDestination = os.path.join(videoDirectory, tail)
		seriesList.append(tail)
	else:
		fileDestination = os.path.join(movieDirectory, tail)
		movieList.append(tail)
	print("moving " + fileSource + " to " + fileDestination)
	shutil.move(fileSource, fileDestination)
	numberOfVideosMigrated += 1

if (numberOfVideosMigrated > 0):
	EmailSummary.sendEmailSummary(seriesList, movieList)

for folder in folderList:
	try:
		shutil.rmtree(folder)
	except Exception:
		pass

print("moved " + str(numberOfVideosMigrated) + " files.")