import os

def getFilesToMigrate(folder, fileTypes, includeSubFolder):
    fileList = []
    """ returns a list of full paths to all files of specified filetype in folder and optionally subfolders. """
    if not folder:
        raise Exception("You must specify a source folder")

    if os.path.exists(folder) and os.path.isdir(folder):
        for subdir in [dirInfo[0] for dirInfo in os.walk(folder)]:
            getFilesToMigrate(os.path.join(folder, subdir), fileTypes, includeSubFolder)
        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for file in files:
            if (len(fileTypes) == 0 or os.path.splitext(file)[1] in fileTypes):
                fileList.append(file)
    else:
        raise Exception(str(folder) + " doesn't exist or isn't a folder.")

    return fileList

getFilesToMigrate("./test/1/", [".mkv"], True)