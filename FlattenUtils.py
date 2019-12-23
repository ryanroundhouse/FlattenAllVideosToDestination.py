import os

def getFilesToMigrate(folder, fileTypes):
    """ returns a list of full paths to all files of specified filetype in folder and optionally subfolders. """
    if not folder:
        raise Exception("You must specify a source folder")

    fileList = []
    if os.path.exists(folder) and os.path.isdir(folder):
        for dirpath,_,filenames in os.walk(folder):
            for f in filenames:
                if len(fileTypes) == 0 or os.path.splitext(f)[1] in fileTypes:
                    fileList.append(os.path.abspath(os.path.join(dirpath, f)))
    else:
        raise Exception(str(folder) + " doesn't exist or isn't a folder.")

    return fileList

getFilesToMigrate("./test/", [".mkv"])