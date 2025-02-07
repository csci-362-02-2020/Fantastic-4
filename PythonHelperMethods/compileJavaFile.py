import os

# This function will just compile a Java file
    # This assumes that the java file is in the same directory
def compileJavaFile(fileName):

    # Compile the Java file
    os.system("javac " + fileName)

# This function will just compile a Java file
    # This assumes that the java file is in a different directory
def compileJavaFileAtLocation(filePath):

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Split file path
    splitFilePath = filePath.split("/")

    # Parse out the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Compile the Java file
    os.system("javac " + fileName)

# File Name
fileName = "TestMethod.java"

# File Path
filePath = "../Test/TestMethod.java"

# Call the function
compileJavaFileAtLocation(filePath)