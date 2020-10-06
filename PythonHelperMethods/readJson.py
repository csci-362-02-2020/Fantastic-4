import os
import json

# This function will just read a Json file
    # This assumes that the Json file is in a different directory
def readJsonAtLocation(filePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    jsonFile = open(fileName)

    jsonData = json.load(jsonFile)

    return jsonData

# File Path
filePath = "../TestAutomation/testCases/compareTo/testCase1.json"

data = readJsonAtLocation(filePath)

print(data["component"])