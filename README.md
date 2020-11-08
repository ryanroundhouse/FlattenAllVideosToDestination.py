# FlattenAllVideosToDestination.py
Move all videos from a single download folder to series folder (if it's an episode) or movies folder (if it's a movie).

Created by Ryan Graham 2018

## Instructions:
Execute script by running 
``` python FlattenAllVideosToDestination.py _source folder_ _series folder_ _movies folder_```

## Output
All video files are moved from the _source folder_ into either _series folder_ or _movies folder_ depending on whether it's a movie or a show.
The script will migrate the following video files by extension (".mp4", ".avi", ".mkv", ".mov", ".mpg", ".wmv")

## Known issues
I never tested overwritting files.

## Unit tests
Execute unit tests by running
``` py -m unittest FlattenUtils_test ```
