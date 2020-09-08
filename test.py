import os
import webbrowser

# Open the file
fileOut = open("test.html", "w")

new = 2 # open in a new tab, if possible

osDIR = os.listdir(os.getcwd())

# Create a list to hold the names of all the folders
folderList = []

# Create a list to hold the names of all the files
fileList = []

# Run the ls command and print the results to the terminal
print("Running ls command...")
lsOutput = os.system("ls")

# Seperate the folders and the files into their correct list
for item in osDIR:
    if(os.path.isdir(item)):
        folderList.append(item)
    else:
        fileList.append(item)

print()
print("Constructing the html file...")

# Print the folders to the html file
fileOut.write("<strong>Folders in current directory:</strong>\n<br />\n\n")

for item in folderList:
    fileOut.write("<h>" + item +"</h>\n<br />\n\n<br />\n\n")

# Print the files to the html file
fileOut.write("<strong>Files in current directory:</strong>\n<br />\n\n")

for item in fileList:
    fileOut.write("<h>" + item +"</h>\n<br />\n\n")

# Close the file
fileOut.close()

# Open the html file in the browser
print("Opening the html file...")
webbrowser.open("test.html", new=new)