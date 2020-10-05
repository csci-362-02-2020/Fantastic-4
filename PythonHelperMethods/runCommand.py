import os

# Runs the given command in Linux terminal
def runCommand(command):

    # Run the command
    os.system(command)

# Changes the directory to the given path
    # Then, runs the given command in Linux terminal
def runCommandAtLocation(command, path):

    # Change the directory to the given path
    os.chdir(path)

    # Run the command
    os.system(command)

runCommandAtLocation("ls", "../TeamExersise")