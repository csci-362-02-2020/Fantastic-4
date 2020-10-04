import os

# This function will just run a Java file

def runJavaFile(fileName):

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

fileName = "TestMethod.java"

# Call the function
runJavaFile(fileName)