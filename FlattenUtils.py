import os
import logging

def getFoldersWithVideoFiles(folder, fileTypes):
    """ returns a list of all folders that contain specified filetype in subfolders of source folder. """
    if not folder:
        raise Exception("You must specify a source folder")

    folderList = []
    if (os.path.exists(folder) and os.path.isdir(folder)):
        for dirpath,_,filenames in os.walk(folder):
            for f in filenames:
                if len(fileTypes) == 0 or os.path.splitext(f)[1] in fileTypes:
                    folderList.append(dirpath)
                    break
    else:
        raise Exception(str(folder) + " doesn't exist or isn't a folder.")

    folderList = sortAscending(folderList)
    logging.info(folderList)
    return folderList

def sortAscending(lst): 
    lst.sort(key=len, reverse=True)
    return lst

def getFilesInFolder(folder, fileTypes):
    """ returns a list of full paths to all files of specified filetype in folder. """
    if not folder:
        raise Exception("You must specify a source folder")
    fileList = []
    for filename in os.listdir(folder):
        if len(fileTypes) == 0 or os.path.splitext(filename)[1] in fileTypes:
            fileList.append(os.path.abspath(os.path.join(folder, filename)))

    return fileList

def getFilesToMigrate(folder, fileTypes):
    """ returns a list of full paths to all files of specified filetype in folder and optionally subfolders. """
    if not folder:
        raise Exception("You must specify a source folder")

    fileList = []
    foldersWithFiles = getFoldersWithVideoFiles(folder, fileTypes)
    for subfolder in foldersWithFiles:
        foundFiles = getFilesInFolder(subfolder, fileTypes)
        for foundFile in foundFiles:
            fileList.append(foundFile)

    return fileList

# getFilesToMigrate("./test/", [".mkv"])