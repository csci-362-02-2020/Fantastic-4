
import os

def copyFile(fromPath, toPath):
    # Change directory to be in the Fantastic-4 directory.
    os.chdir("..")

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


filePath = "stem-master/org.eclipse.stem.core/src/org/eclipse/stem/core/math/BinomialDistributionUtil.java"
toLocation = "Test/"

# Call the function
copyFile(filePath, toLocation)