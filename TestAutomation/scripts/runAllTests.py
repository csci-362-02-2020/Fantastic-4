import os
import json

####################################################################################################
####################################################################################################
####################################################################################################

# READ JSON FILE

# This method will read a JSON file and return a JSON object

# Input: file path to JSON file
# Output: JSON object

def readJsonAtLocation(filePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    jsonFile = open(fileName)

    jsonData = json.load(jsonFile)

    # Change the directory back to the way it was...
    os.chdir("../../scripts")

    return jsonData

####################################################################################################
####################################################################################################
####################################################################################################

# COPY FILE and DELETE FIRST LINE

# Input: pathFrom, pathTo
def copyFromProjectToTestCaseExe(pathFrom, pathTo):
    
    # Create the command to copy the file
    command = "cp " + pathFrom + " " + pathTo

    # Run the command
    os.system(command)
    os.chdir(pathTo)

    # Split file path
    splitFilePath = pathFrom.split("/")

    # Little trickery (slight of hand) =) to get rid of the first two lines in the file which is the package declaration.
        # The package declaration will not let us compile the java file in this directory
    os.system("cat " + splitFilePath[len(splitFilePath)-1] + " > " + "temp.txt")
    os.system("tail -n +3 temp.txt > " + splitFilePath[len(splitFilePath)-1])
    os.system("rm temp.txt")

####################################################################################################
####################################################################################################
####################################################################################################

# RUN TEST CASE

# This method will run a test case at the given file path and print the output to a result file.

# Input: file path to test case
# Ouput: result of test printed to file
def runTestCase(testCaseJSON):
    
    # Get the path to the component
    componentPath = testCaseJSON["component"]

    # Get the driver path and the driver folder
    driverPath = testCaseJSON["driver"]
    driverFolder = driverPath[0:driverPath.rindex("/")]

    # Copy the Java project to the Test Case Executables folder
    copyFromProjectToTestCaseExe(componentPath, driverFolder)


####################################################################################################
####################################################################################################
####################################################################################################

# MAIN

def main():
    # lnFactorial Method

    # Test case 1
    lnFactorialTestOne = readJsonAtLocation("../testCases/computeNoise/testCase1.json")
    runTestCase(lnFactorialTestOne)

####################################################################################################
####################################################################################################
####################################################################################################

main()