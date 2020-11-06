import os
import json
import webbrowser

# Open the report file
reportFile = open("reports/testReport.html", "w")

####################################################################################################
####################################################################################################
####################################################################################################

def writeMethodResults(methodName):
    pathToJSON = "testCases/" + methodName + "/"
    testOne = readJsonAtLocation(pathToJSON + "testCase1.json")
    testTwo = readJsonAtLocation(pathToJSON + "testCase2.json")
    testThree = readJsonAtLocation(pathToJSON + "testCase3.json")
    testFour = readJsonAtLocation(pathToJSON + "testCase4.json")
    testFive = readJsonAtLocation(pathToJSON + "testCase5.json")

    # Construct the report for the first method
    resultsFilePath = "temp/" + methodName + "/"

    reportFile.write("<h3 style=\"color:blue;\">" + methodName + "()</h3>\n")

    writeTestResults(resultsFilePath + "testCase1results.txt", "one", testOne)
    writeTestResults(resultsFilePath + "testCase2results.txt", "two", testTwo)
    writeTestResults(resultsFilePath + "testCase3results.txt", "three", testThree)
    writeTestResults(resultsFilePath + "testCase4results.txt", "four", testFour)
    writeTestResults(resultsFilePath + "testCase5results.txt", "five", testFive)

    reportFile.write("<hr>\n\n")

####################################################################################################
####################################################################################################
####################################################################################################

def writeTestResults(filePath, testNum, testJson):
    
    resultsFile= open(filePath)

    i = 0

    for line in resultsFile:
        if (i == 0):
            reportFile.write("<h4>" + line.strip() + "</h4>\n")
        elif ("passed" in line):
            reportFile.write("<p>Test " + testNum + "<i style=\"color:green;\"> passed</i>!</p>\n")
        elif ("failed" in line):
            reportFile.write("<p>Test " + testNum + "<i style=\"color:red;\"> failed</i>!</p>\n")
        else:
            reportFile.write("<p>" + line.strip() + "</p>\n")

        i += 1

    reportFile.write("\n\n\n")

####################################################################################################
####################################################################################################
####################################################################################################

def constructReport(methodNames):
    print("Constructing final report")

    # Write the first line
    reportFile.write("<h1>Test Results</h1>\n\n")
    reportFile.write("<hr>\n\n")
    
    for method in methodNames:
        writeMethodResults(method)

####################################################################################################
####################################################################################################
####################################################################################################

def testMethod(methodName):
    pathToJSON = "testCases/" + methodName + "/"
    testOne = readJsonAtLocation(pathToJSON + "testCase1.json")
    testTwo = readJsonAtLocation(pathToJSON + "testCase2.json")
    testThree = readJsonAtLocation(pathToJSON + "testCase3.json")
    testFour = readJsonAtLocation(pathToJSON + "testCase4.json")
    testFive = readJsonAtLocation(pathToJSON + "testCase5.json")

    # You only run this once per method...
    moveProjectFileandCompile(testOne)

    # You only run this once per method...
    cleanOutTempFoder(testOne)

    print("Testing " + methodName + ":")

    # Test case 1
    print("Running test 1")
    runTestCase(testOne)
    # Test case 2
    print("Running test 2")
    runTestCase(testTwo)
    # Test case 3
    print("Running test 3")
    runTestCase(testThree)
    # Test case 4
    print("Running test 4")
    runTestCase(testFour)
    # Test case 5
    print("Running test 5\n")
    runTestCase(testFive)

    # You only run this once per method...
    cleanUpTestCaseExe(testOne)

####################################################################################################
####################################################################################################
####################################################################################################

# CLEAN OUT TEMP FOLDER

# This method will clean out the TEMP folder

# Input: Test JSON file
# Output: NONE (clean TEMP folder)

def cleanOutTempFoder(testCaseJSON):
    # Run the test case and print the results to a file
    methodName = testCaseJSON["method"]
    id = testCaseJSON["id"]
    
    # Build the file path
    tempFolderFullPath = "temp/" + methodName + "/testCase" + str(id) + "results.txt"
    tempFolder = tempFolderFullPath[0:tempFolderFullPath.rindex("/")]
    
    # Go to the directory
    os.chdir(tempFolder)

    # Remove everything from the temp folder
    os.system("rm *")

    # Change the directory back to the way it was...
    os.chdir("../../")

####################################################################################################
####################################################################################################
####################################################################################################

# CLEAN UP TEST CASE EXECUTABLES FOLDER

# Input: JSON file of test case
# Output: NONE (clean folder)

def cleanUpTestCaseExe(testCaseJSON):

    # Get the path to the component
    componentPath = testCaseJSON["component"]

    # Get the driver path and the driver folder
    driverPath = testCaseJSON["driver"]
    driverFolder = driverPath[0:driverPath.rindex("/")]

####################################################################################################

    # Compile project file
    splitcomponentPath = componentPath.split("/")
    nameOfProjectJavaFile = splitcomponentPath[len(splitcomponentPath)-1]
    newProjectLocation = driverFolder + "/" + nameOfProjectJavaFile

    # Change the directory to the given path
    os.chdir(driverFolder)

    # Split file path
    splitFilePath = newProjectLocation.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Split the file name
    splitFileName = fileName.split(".")

    # Remove all files with that name, regardless of extension
    os.system("rm " + splitFileName[0] + ".*")

    # Change the directory back to the way it was...
    os.chdir("../../")

####################################################################################################
####################################################################################################
####################################################################################################

# MOVE PROJECT FILE and COMPILE FILE

# This method will move the project file in the correct directory and compile the file
# Input: testCaseJSON
# Output: NONE

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

# Input: filePath, input, outputFilePath
# Output: results printed to file

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
    command += "> " + "../../" + outputFilePath

    # Run the compiled file
    os.system(command)

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

    # Change the directory back to the way it was...
    os.chdir("../../")

####################################################################################################
####################################################################################################
####################################################################################################

# COMPILE JAVA FILE at LOCATION

# This method will compile a java file at a particular location

# Input: filePath of Java File
# Output: NONE

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
    os.chdir("../../")

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
    os.chdir("../../")

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
    os.chdir("../../")

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
    methodName = testCaseJSON["method"]
    inputArray = [input, output]
    id = testCaseJSON["id"]

    # Build the output file
    outFilePath = "temp/" + methodName + "/testCase" + str(id) + "results.txt"
    compileAndRunJavaFileAtLocationWithInputOutputToFile(driverPath, inputArray, outFilePath)

####################################################################################################
####################################################################################################
####################################################################################################

# MAIN

def main():

####################################################################################################

    # Get the method names
    methodNames = []

    os.system("ls testCases > methodNames.txt")

    tempFile = open("methodNames.txt", "r")

    for line in tempFile:
        methodNames.append(line.strip())

    os.system("rm methodNames.txt")

    for method in methodNames:
        testMethod(method)

####################################################################################################

    # Construct the HTML file and open it in the browser
    constructReport(methodNames)

    # Open the html file in the browser
    new = 2 # open in a new tab, if possible
    print("Opening the html file")
    webbrowser.open("reports/testReport.html", new=new)

####################################################################################################
####################################################################################################
####################################################################################################

main()