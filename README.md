# PasswordStrengthChecker
Overview
The Password Strength Checker is a simple application that evaluates the strength of a password based on various criteria. It provides a rating out of 5 levels, estimates the time it would take to crack the password using brute force, and offers suggestions to improve password strength. The application also includes a feature to toggle password visibility for ease of use.

Features
Password Strength Rating: Rates the password strength from 'Very Weak' to 'Very Strong'.
Crack Time Estimation: Provides an estimated time to crack the password.
Suggestions: Offers advice on how to improve password strength.
Show Password Option: Allows users to view their password to recheck.
Requirements
Python 3.x
Tkinter (usually comes pre-installed with Python)
PyInstaller (for converting the script to an executable)
Installation
Clone or Download: Download the source code file named styled_password_checker.py.

Install Dependencies:
Ensure you have Python 3 installed. Then, install PyInstaller if you want to convert the script to an executable:

sh
Copy code
pip install pyinstaller
Usage
Run the Script:
Open your terminal or command prompt, navigate to the directory where styled_password_checker.py is located, and run:

sh
Copy code
python styled_password_checker.py
Using the Application:

Enter your password into the input field.
Click the "Check Password" button to see the results, including strength rating, crack time estimation, and suggestions.
Converting to Executable
To convert the Python script to a standalone executable, follow these steps:

Navigate to Script Directory:
Open your terminal or command prompt and navigate to the directory where styled_password_checker.py is located.

Create the Executable:
Run the following command:

sh
Copy code
pyinstaller --onefile --windowed styled_password_checker.py
--onefile: Creates a single executable file.
--windowed: Prevents the terminal window from appearing when running the GUI application.
Locate the Executable:
After running the command, PyInstaller will create a dist folder in the same directory. Your executable file will be inside this folder.

Distribute:
You can now distribute the executable file to other systems that do not have Python installed.

Attribution
Developed by Rachit Nahata.
