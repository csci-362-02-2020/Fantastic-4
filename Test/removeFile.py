import os

# This function will remove a file
    # This assumes that the file is in the same directory
def removeFile(fileName):
    # Split the file name
    splitFileName = fileName.split(".")

    # Remove all files with that name, regardless of extension
    os.system("rm " + splitFileName[0] + ".*")

# This function will remove a file
    # This assumes that the java file is in a different directory
def removeFileAtLocation(fileName):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Split the file name
    splitFileName = fileName.split(".")

    # Remove all files with that name, regardless of extension
    os.system("rm " + splitFileName[0] + ".*")

# File Name
fileName = "BinomialDistributionUtil.java"

# File Path
filePath = "../filesToTest/LatLong.java"

# Call the function
removeFileAtLocation(filePath)