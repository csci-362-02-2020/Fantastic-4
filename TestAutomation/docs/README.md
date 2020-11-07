# README
Steps taken to run all tests...

*If you already have a functioning Linux VM you can skip to step 6.*

## Steps:
1. Install Oracle VM VirtualBox.
	https://www.virtualbox.org/wiki/Downloads 
2. Download a Linux ISO file.
	https://ubuntu.com/download/desktop/thank-you?version=20.04.1&architecture=amd64
3. Import the ISO file into Virtual Box.
4. Start the Linux VM.
5. Install the operating system.
6. Open a browser and navigate to the Fantastic 4 repo page.
	https://github.com/csci-362-02-2020/Fantastic-4
7. Save the repository as a zip file.
8. Unzip the repo to any location on your VM.
9. Open a terminal and navigate to where the zipped repo is stored.
10. Run the following command to unzip the repo...
	a. unzip Fantastic-4-master.zip
12. Navigate to the folder that houses the unzipped repo.
13. Type the following commands to install python and java…
	a. sudo apt-get update
	b. sudo apt-get install python3.9
	c. sudo apt-get install openjdk-8-jdk
14. Type the following commands to run all tests…
	a. cd Fantastic-4-master/TestAutomation/
	b. python3.9 ./scripts/runAllTests.py

*Note: The program will open an html file in the browser...*
*You may have to hit the refresh button a few times for the page to load.*
