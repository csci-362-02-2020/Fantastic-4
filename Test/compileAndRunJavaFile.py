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

    # Split file path
    splitFilePath = filePath.split("/")

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Assign the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Compile the file
    os.system("javac " + fileName)

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

# File Name
fileName = "TestMethod.java"

# File Path
filePath = "../filesToTest/LatLong.java"

# Call the function
compileAndRunJavaFile(fileName)