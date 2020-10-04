import os

# This function will just compile a Java file

def compileJavaFile(fileName):

    # Compile the Java file
    os.system("javac " + fileName)

fileName = "TestMethod.java"

# Call the function
compileJavaFile(fileName)