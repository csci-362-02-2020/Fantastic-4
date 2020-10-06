import os

def stringInFileAtLocation(filePath, string):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Open the file
    readFile = open(fileName, "r")

    # Check if the file has the specified string
    for line in readFile:
        if(string in line):
            return True
    
    return False

path = "../Test/BinomialDistributionUtil.java"

string = "class"

value = stringInFileAtLocation(path, string)

print(value)