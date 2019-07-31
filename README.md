# FlattenAllVideosToDestination.py
Flatten all videos from a folder structure to a specific folder.
I created this script to collapse all the subfolders each with a single video file into a single folder so that I can easily apply an action to all videos in a series (delete, archive, etc...)

Created by Ryan Graham 2018

## Instructions:
1. Execute script by running '> python FlattenAllVideosToDestination.py _source folder_ _destination folder_'

## Output
All files are moved from the _source folder_ structure into the _destination folder_.

2 csv files are created in the execution directory during execution.
1. notMigrated.csv - this file contains a listing of all files that were skipped.
2. migrated.csv - this file contains a listing of all files that were migrated.

## Known issues
1. I never tested overwritting files.
