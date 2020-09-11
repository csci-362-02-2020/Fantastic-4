import os
import webbrowser

# Open the file
fileOut = open("outFile.html", "w")
StyleFileIn = open("style.html", "r")

# Write the style to the html file (This style was found here... https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro)
for line in StyleFileIn:
    fileOut.write(line)
fileOut.write("\n\n")

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

# Html for the table
fileOut.write("<table>\n\n")

# Print the folders to the html file
fileOut.write("<tr><th><strong>Folders in current directory:</strong></tr></th>\n\n")

for item in folderList:
    fileOut.write("<tr><td>" + item +"</td></tr>\n\n")

# Html for the table
fileOut.write("</table>\n\n<br />\n\n")

# Html for the table
fileOut.write("<table>\n\n")

# Print the files to the html file
fileOut.write("<tr><th><strong>Files in current directory:</strong></tr></th>\n\n")

for item in fileList:
    fileOut.write("<tr><td>" + item +"</td></tr>\n\n")

# Html for the table
fileOut.write("</table>\n\n<br />\n\n")

# Close the file
fileOut.close()

# Open the html file in the browser
print("Opening the html file...")
webbrowser.open("outFile.html", new=new)