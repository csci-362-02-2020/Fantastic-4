import os

# This function will just run a Java file
    # This assumes that the file is in the same directory
def runJavaFile(fileName):

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

# This function will just run a Java file
    # This assumes that the java file is in a different directory
def runJavaFileAtLocation(filePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

# This function will just run a Java file
    # This assumes that the java file is in a different directory
    # Input is given to Java File
def runJavaFileAtLocationWithInput(filePath, input):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Split the file name
    splitFileName = fileName.split(".")

    # Contsrtuct the command
    command = "java " + splitFileName[0] + " "

    # Append the input items to the command
    for item in input:
        command += item + " "

    # Run the compiled file
    os.system(command)

# This function will just run a Java file
    # This assumes that the java file is in a different directory
    # Input is given to Java File
def runJavaFileAtLocationWithInputOutputToFile(filePath, input, outputFilePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Split the file name
    splitFileName = fileName.split(".")

    # Contsrtuct the command
    command = "java " + splitFileName[0] + " "

    # Append the input items to the command
    for item in input:
        command += item + " "

    # Add the output file to the command
    command += "> " + outputFilePath

    # Run the compiled file
    os.system(command)

# File Path
fileName = "TestMethod.java"

# File Path
filePath = "../Test/TestMethod.class"

# Input
input = ["3", "1.791759469228055"]

# Out file
outputFilePath = "../TestAutomation/oracles/lnFactorial/testCase1Oracle.txt"

# Call the function
runJavaFileAtLocationWithInputOutputToFile(filePath, input, outputFilePath)