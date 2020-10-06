import os

# Change the directory to the specified path
def changeDirectory(path):
    
    # Change the directory    
    os.chdir(path)

path = "../Test"

changeDirectory(path)