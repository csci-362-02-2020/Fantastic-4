import os
import json

####################################################################################################
####################################################################################################
####################################################################################################

def moveProjectFileandCompile(testCaseJSON):
    # Get the path to the component
    componentPath = testCaseJSON["component"]

    # Get the driver path and the driver folder
    driverPath = testCaseJSON["driver"]
    driverFolder = driverPath[0:driverPath.rindex("/")]

    # Copy the Java project to the Test Case Executables folder
    copyFromProjectToTestCaseExe(componentPath, driverFolder)

####################################################################################################

    # Compile project file
    splitcomponentPath = componentPath.split("/")
    nameOfProjectJavaFile = splitcomponentPath[len(splitcomponentPath)-1]
    newProjectLocation = driverFolder + "/" + nameOfProjectJavaFile
    compileJavaFileAtLocation(newProjectLocation)

####################################################################################################
####################################################################################################
####################################################################################################

# COMPILE and RUN JAVA FILE PRINT RESULTS to FILE

# This method will compile and run a java file with command line arguments and print the ouput to a file

def compileAndRunJavaFileAtLocationWithInputOutputToFile(filePath, input, outputFilePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Compile the file
    os.system("javac " + fileName)

    # Split the file name
    splitFileName = fileName.split(".")

    # Contsrtuct the command
    command = "java " + splitFileName[0] + " "

    # Append the input items to the command
    for item in input:
        command += item + " "

    # Add the output file to the command
    command += "> " + "../" + outputFilePath

    # Run the compiled file
    os.system(command)

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

    # Change the directory back to the way it was...
    os.chdir("../../scripts")

####################################################################################################
####################################################################################################
####################################################################################################

# COMPILE JAVA FILE at LOCATION

# This method will compile a java file at a particular location

# Input: filePath of Java File
# Output: None

def compileJavaFileAtLocation(filePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Compile the Java file
    os.system("javac " + fileName)

    # Change the directory back to the way it was...
    os.chdir("../../scripts")

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

# COPY FILE and DELETE FIRST TWO LINES

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
    
    # Change the directory back to the way it was...
    os.chdir("../../scripts")

####################################################################################################
####################################################################################################
####################################################################################################

# RUN TEST CASE

# This method will run a test case at the given file path and print the output to a result file.

# Input: file path to test case
# Ouput: result of test printed to file
def runTestCase(testCaseJSON):

    # Get the path to the driver
    driverPath = testCaseJSON["driver"]

    # Run the test case and print the results to a file
    input = testCaseJSON["input"]
    output = testCaseJSON["output"]
    inputArray = [input, output]
    outFilePath = testCaseJSON["result"]
    compileAndRunJavaFileAtLocationWithInputOutputToFile(driverPath, inputArray, outFilePath)

####################################################################################################
####################################################################################################
####################################################################################################

# MAIN

def main():
    # lnFactorial Method
    lnFactorialTestOne = readJsonAtLocation("../testCases/lnFactorial/testCase1.json")
    lnFactorialTestTwo = readJsonAtLocation("../testCases/lnFactorial/testCase2.json")
    lnFactorialTestThree = readJsonAtLocation("../testCases/lnFactorial/testCase3.json")
    lnFactorialTestFour = readJsonAtLocation("../testCases/lnFactorial/testCase4.json")
    lnFactorialTestFive = readJsonAtLocation("../testCases/lnFactorial/testCase5.json")

    # You only run this once per method...
    moveProjectFileandCompile(lnFactorialTestOne)

    # Test case 1
    runTestCase(lnFactorialTestOne)
    # Test case 2
    runTestCase(lnFactorialTestTwo)
    # Test case 3
    runTestCase(lnFactorialTestThree)
    # Test case 4
    runTestCase(lnFactorialTestFour)
    # Test case 5
    runTestCase(lnFactorialTestFive)

####################################################################################################
####################################################################################################
####################################################################################################

main()