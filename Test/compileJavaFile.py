import os

# This function will just compile a Java file
    # This assumes that the java file is in the same directory
def compileJavaFile(fileName):

    # Compile the Java file
    os.system("javac " + fileName)

# This function will just compile a Java file
    # This assumes that the java file is in a different directory
def compileJavaFileAtLocation(filePath):

    # Split file path
    splitFilePath = filePath.split("/")

    # Change the directory to the given path
    os.chdir(filePath[0:filePath.rindex("/")])

    # Assign the name of the file
    fileName = splitFilePath[len(splitFilePath)-1]

    # Compile the Java file
    os.system("javac " + fileName)

# File Name
fileName = "TestMethod.java"

# File Path
filePath = "../filesToTest/LatLong.java"

# Call the function
compileJavaFile(fileName)