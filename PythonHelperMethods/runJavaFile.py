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

# File Path
fileName = "TestMethod.java"

# File Path
filePath = "../Test/TestMethod.class"

# Call the function
runJavaFileAtLocation(filePath)