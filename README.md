<span style="color:#fff; font-family: 'Times New Roman'; font-size: 12em;">

# TheEqualizer-CSEC475-2171-Lee
Project utilizes the Nessus API to pull scans from server to record numbers and display charts and graphs using plotly.

The Equalizer creates additional visualization for Nessus Reports. It helps people who are not technologically inclined better understand the data the Nessus Report displays. This project is designed to help companies who are hired to perform penetration testing and vulnerability scans who use the Nessus Vulnerability Scanner; give their client better visualizations for both the pentester and the client.

# Current Version
1. Operating System - MacOS High Sierra 10.13
2. Nessus Server Version - 6.11.2
3. Python Version - 2.7.14


# Contact Information
For Updates/Modifications/Applause/etc.
<ul>
<li>Creator: Wesley Lee</li>
<li>Email: wtl5736@rit.edu</li>
</ul>

# Table of Contents
		A. Create a Plotly Account
		B. How to Find Plotly API Key
		C. How to Install Requirements
		D. How to Install Nessus
			Section 1. MacOS
			Section 2. Linux
		E. How to Install Python 2.7.14
		F. How to start The Equalizer
			Section 1. MacOS and Linux
		G. How to Find Nessus IP/URL, Port Number, and Report ID


## A. Create a Plotly Account

1. Go to https://plot.ly/
2. Click on "Log In" at the top right of the webpage
3. If you already have an account sign in; if you don't click on 
	the "Sign Up" tab.
4. Fill out the necessary log in information


## B. How to Find Plotly API Key

1. Login to your plotly account at https://plot.ly/
2. Once logged in you should see your username at the top right of the 
	webpage; hover your cursor over you username to see the drop down menu
3. Click on "Settings"
4. On the left side of the webpage click on "API Keys"
5. Under username on the right side of the webpage you should see 
	the section "API Keys"
6. The API Key is hidden; click on "Regenerate Key"
7. This will regenerate a new API Key
8. You will need your username and  the API Key when you run setup.py
9. Information:
   * Red Arrow = Plotly Username
   * Blue Arror = Plotly API Key

![picture](/Pictures/Plotly_Info.png)


## C. How to Install Requirements

1. Open Terminal 
2. Change the directory to TheEqualizer-CSEC475-2171-Lee
	-> "cd TheEqualizer-CSEC475-2171-Lee"
3. Run the setup program
	-> "sudo python setup.py"
4. setup.py will install the necessary python modules and will ask your for 
	your plotly username and api_key (To found your api_key look 
	at Section B in the table of contents)
5. Enter in your username and API Key for Plotly
6. After the installation is finished; you will be prompted to 
	run The Equalizer program
7. Enter 'y' to run the program or 'n' to exit


## D. How to Install Nessus

###  Section 1. MacOS

1.  Go to https://www.tenable.com/products/nessus/select-your-operating-system
2.  On left side of the webpage click "MacOS"
3.  Choose your version of MacOS (click on the .dmg file to download)
	 a. After downloading the .dmg file, if you dont have an Activation Code click on 
		"Get an Activation Code" below where you select your operating system
	 b. Choose the version of Nessus you want (Home, Professional, or Manager)
	 c. You should be emailed your activation key
4.  Run the Nessus .dmg file to install
5.  Once the Tenable Nessus Server Installer is opened and running click "Continue"
6.  Then click "Continue" and "Agree" the License Agreement for Nessus
7.  Finally, click "Install" (Requires Administrator Password)
8.  After the installation is complete click "Close"
9.  You can select "Move to Trash" unless you want to keep the .dmg file
10. This will open a browser windows; click "Connect via SSL"
11. The browser will tell you the site isn't safe; but go and click "Advanced"; 
		depending on your browser add the exception or proceed to the localhost
12. Next it will bring you to the Nessus Welcome screen; click "Continue"
13. Next enter the "Username" and your "Password" for the Administrator account 
		for Nessus, then click "Next"
14. Make sure the Registration is set to "Nessus (Home, Professional, or Manager)"
15. Then enter in your activation code that should've been emailed to you, then click "Next"
16. Nessus will download the correct version based on the activation code entered
17. After the installation is finished, log in with the administrator account 
		you created when installing Nessus


###  Section 2. Linux

1.  Go to https://www.tenable.com/products/nessus/select-your-operating-system
2.  On left side of the webpage click "Linux"
3.  Choose your distribution of Linux you're running (click on the .dmg file to download)
	  a. After downloading the .dmg file, if you dont have an Activation 
			Code click on "Get an Activation Code" below where you select your operating system
	  b. Choose the version of Nessus you want (Home, Professional, or Manager)
	  c. You should be emailed your activation key
4.  Go to the folder where you downloaded the Nesuss .rpm file in a terminal
5.  Enter "sudo rpm -ivh Nessus-version_number.rpm" (Requires Administrator Password)
	 - For example (CentOS), "sudo rpm -ivh Nessus-6.11.2-es7.x86_64.rpm"
6.  Enter in your Administrator password for the system
7.  After Nessus has finished installing you will need to start the server, 
		enter "systemctl start nessusd.service"
	 - To verify that the server is running enter 
		"systemctl status nessusd.service", you should see "active (running)" in green text
8.  Next, open https://localhost.localdomain:8834/ in a web browser
9.  The browser will tell you the site isn't safe; but go and click "Advanced"; 
		depending on your browser add the exception or proceed to the localhost
10.  Next it will bring you to the Nessus Welcome screen; click "Continue"
11. Next enter the "Username" and your "Password" for the Administrator 
		account for Nessus, then click "Next"
12. Make sure the Registration is set to "Nessus (Home, Professional, or Manager)"
13. Then enter in your activation code that should've been emailed to you, then click "Next"
14. Nessus will download the correct version based on the activation code entered
15. After the installation is finished, log in with the administrator account 
		you created when installing Nessus

## E. How to Install Python 2.7.14

1. Open a terminal and change the directory to the Desktop
  * "cd ~/Desktop"
2. Enter, "wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz --no-check-certificate"
3. Then enter, "tar -xzf Python-2.7.14.tgz"
4. After the tar file is decompressed change to the directory that was extracted
  * "cd Python-2.7.14"
5. Next, enter in the terminal, "sudo ./configure"
6. Then, enter in the terminal, "sudo make install"
7. Finally, enter in the terminal, "sudo make altinstall"
8. To test python is the correct version, enter in the terminal, "python"
9. This should open a python terminal and at the top it should display "Python 2.7.14"

## F. How to start The Equalizer

1. Download the tool at https://github.com/wtl5736/TheEqualizer-CSEC475-2171-Lee.git; you can either:
  * Open a terminal and enter "git clone https://github.com/wtl5736/TheEqualizer-CSEC475-2171-Lee.git"; or
  * Download the zip file at https://github.com/wtl5736/TheEqualizer-CSEC475-2171-Lee.git
3. Once the tool is downloaded, Open a terminal
2. Change the directory to TheEqualizer-CSEC475-2171-Lee
	-> "cd TheEqualizer-CSEC475-2171-Lee"
3. Make sure you run setup.py before running The_Equalizer.py
  * "sudo python setup.py", then
  * "sudo python The_Equalizer.py"'
4. Enter the command "sudo python The_Equalizer.py" to run the program

**** You only Need to run setup.py the first time, unless you use a different account for Plotly **


## G. How to Find Nessus IP/URL, Port Number, and Report ID
1. Open your the Nessus Server in a web browser
2. Log in with the correct credentials
3. Click on the scan you are trying to access
4. Information:
  * Red Arrow = Nessus Server IP/URL Address
  * Blue Arrow = Nessus Server Port Number
  * Pink Arrow = Report ID Number

![picture](/Pictures/Nessus_Info.png)


</span>
