import os

# This function will compile and run a Java file

def compileAndRunJavaFile(fileName):
    # Compile the file
    os.system("javac " + fileName)

    # Split the file name
    splitFileName = fileName.split(".")

    # Run the compiled file
    os.system("java " + splitFileName[0])

    # Remove the class file
    os.system("rm " + splitFileName[0] + ".class")

fileName = "TestMethod.java"

# Call the function
compileAndRunJavaFile(fileName)