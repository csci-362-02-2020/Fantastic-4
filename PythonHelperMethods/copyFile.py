
import os

def copyFileAndDeleteFirstLine(fromPath, toPath):
    
    # Create the command to copy the file
    command = "cp " + fromPath + " " + toPath

    # Run the command
    os.system(command)
    os.chdir(toPath)

    # Split file path
    splitFilePath = filePath.split("/")

    # Little trickery (slight of hand) =) to get rid of the first two lines in the file which is the package declaration.
        # The package declaration will not let us compile the java file in this directory
    os.system("cat " + splitFilePath[len(splitFilePath)-1] + " > " + "temp.txt")
    os.system("tail -n +3 temp.txt > " + splitFilePath[len(splitFilePath)-1])
    os.system("rm temp.txt")

def copyFile(fromPath, toPath):

    # Create the command to copy the file
    command = "cp " + fromPath + " " + toPath

    # Run the command
    os.system(command)
    os.chdir(toPath)

filePath = "../TeamExersise/outFile.html"
toLocation = "."

# Call the function
copyFileAndDeleteFirstLine(filePath, toLocation)