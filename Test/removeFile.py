import os

def removeFile(fileName):
    # Split the file name
    splitFileName = fileName.split(".")

    # Remove all files with that name, regardless of extension
    os.system("rm " + splitFileName[0] + ".*")

fileName = "BinomialDistributionUtil.java"

# Call the function
removeFile(fileName)