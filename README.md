
GoNoGo Application
This is a simple Tkinter-based application that calculates the time you can leave work on Friday given your work hours from Monday to Thursday and your start time on Friday.

Features
Input work hours for Monday to Thursday.
Input the start time for Friday.
Calculate and display the time to go home on Friday based on a total work time of 41.5 hours.

Requirements:
- Python 3.x
- Tkinter (usually included with Python)

Installation:
1. Clone the repository or download the source code.
2. Ensure you have Python installed on your system.
3. Run the application using the command:

python3 gonogo.py

Usage:
1. Run the application.
2. Enter your work hours for each day from Monday to Thursday in decimal format.
3. Enter your start time for Friday in HH:MM format.
4. Click the "Calculate GoNoGo" button.
5. A message box will display the hours worked for each day, the start time on Friday, and the calculated go home time on Friday.

Code Explanation:
- The application consists of several functions and a Tkinter-based GUI:
- 'show_message():' This function is called when the "Calculate GoNoGo" button is pressed. It retrieves the   input times, calculates the total work hours, and determines the time to leave on Friday.
- 'calc_GoHomeTime(friday_start, remaining_hours):' This function calculates the go home time based on the Friday start time and the remaining hours needed to complete 41.5 hours.
- 'convert_decimal_hours_to_time(value):' This function converts decimal hours into hours and minutes format.

The GUI is created using Tkinter, with labels and entry widgets for each weekday and a button to trigger the calculation.

Example
I
f you input the following hours:

Monday: 8.5
Tuesday: 8.5
Wednesday: 8.5
Thursday: 8.5
And the start time on Friday is 07:30, the application will calculate and display the go home time on Friday based on the remaining hours needed to complete 41.5 hours.

License
This project is licensed under the MIT License.

