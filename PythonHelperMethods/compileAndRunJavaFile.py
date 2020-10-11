import os

# This function will compile and run a Java file
    # This assumes that the java file is in the same directory
def compileAndRunJavaFile(fileName):
    # Compile the file
    os.system("javac " + fileName)

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

# This function will compile and run a Java file
    # This assumes that the java file is in a different directory
def compileAndRunJavaFileAtLocation(filePath):

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

    # Run the compiled file
    os.system("java " + splitFileName[0])

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

# This function will compile and run a Java file
    # This assumes that the java file is in a different directory
    # Input is given to Java File
def compileAndRunJavaFileAtLocationWithInput(filePath, input):

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

    # Run the compiled file
    os.system(command)

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

# This function will compile and run a Java file
    # This assumes that the java file is in a different directory
    # Input is given to Java File
    # Output to file at given path
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
    command += "> " + outputFilePath

    # Run the compiled file
    os.system(command)

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

# File Name
fileName = "TestMethod.java"

# File Path
filePath = "../TestAutomation/testCasesExecutables/lnFactorial/testCase4.java"

# Input
input = ["1", "0"]

# Out file
outputFilePath = "../../oracles/lnFactorial/testCase4Oracle.txt"

# Call the function
compileAndRunJavaFileAtLocationWithInputOutputToFile(filePath, input, outputFilePath)