# FlattenAllVideosToDestination.py
Flatten all videos from a folder structure to a specific folder.
I created this script to collapse all the subfolders each with a single video file into a single folder so that I can easily apply an action to all videos in a series (delete, archive, etc...)

Created by Ryan Graham 2018

## Instructions:
Execute script by running 
``` python FlattenAllVideosToDestination.py _source folder_ _destination folder_```

## Output
All video files are moved from the _source folder_ structure into the _destination folder_.
The script will migrate the following video files by extension (".mp4", ".avi", ".mkv", ".mov", ".mpg", ".wmv")

## Known issues
I never tested overwritting files.

## Unit tests
Execute unit tests by running
``` py -m unittest FlattenUtils_test ```
