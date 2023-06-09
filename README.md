﻿# Hackaton_2
This code is designed to perform a task based on the following requirements using Python:

Task 01 - Message Generator
As the end of the year approaches, imagine you are a teacher who needs to send a message to each of your students, reminding them of missing assignments and their final grade.

Instead of manually writing emails to each student, you decide to automate the process using Python. The student information is stored in a spreadsheet, with each student having a first name, last name, number of missing assignments, and current grade.

The code is divided into several stages:

Stage 1:
In this stage, a test code is created to understand the flow of the task.

The script does the following:

Prompts the user to enter test data three times: names, missing assignments, and grades.
Creates a template message.
Displays the message for each student with the correct values. The potential grade is calculated as the current grade plus 1.
Sets a common completion date for all students.
Stage 2:
In this stage, a CSV file named "students.csv" is created with student data. The file follows the format: [class],[first name],[last name],[missing assignments],[grade]. For example: "3A,Adam,Kowalski,3,4".

Stage 3:
Inside the script, a function is created to read data from the "students.csv" file. The CSV file is treated as a plain text file using the csv module.

The function:

Reads the file correctly.
Handles the error in case the file is not found.
Creates a data structure based on the file data, such as three lists: names, missing assignments, and grades.
Stage 4:
Replaces the hardcoded message with a function that reads the message from a file named "message.txt". The content of the message can be modified as needed.
Uses the if __name__ == '__main__' expression to separate the executed code from function definitions.
Extension:
If the file contains unexpected values, such as a non-numeric grade, the code handles the error and assigns a grade of 0.
The code can explore the csv module to facilitate file handling and parsing.
Additionally, the code includes examples of error handling and JSON data formatting.

Feel free to ask any questions or seek clarification if needed.
