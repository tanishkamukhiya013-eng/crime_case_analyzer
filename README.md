\# Crime Case Analyzer



\## Project Overview



Crime Case Analyzer is a lightweight, command-line Python application designed to organize and manage fictional crime case records.



The application allows users to add case details, view stored cases, search for a case using its Case ID, update case status, delete cases, and calculate a simple priority based on evidence count.



This project demonstrates the practical use of core Python concepts such as functions, conditional statements, lists, file handling, CSV data storage, and basic automated testing.



\## Features



\- Case Registration: Add a new case with Case ID, crime type, location, suspect name, and evidence count.

\- Case Viewing: Display all stored case records.

\- Case Search: Search for a case using its Case ID.

\- Status Update: Update a case as Open, Under Investigation, or Solved.

\- Case Resolution: Display a confirmation message when a case is marked as Solved.

\- Case Deletion: Delete an existing case using its Case ID.

\- Priority Analysis: Assign High, Medium, or Low priority based on evidence count.

\- Persistent Storage: Save and load case records using a CSV file.

\- Basic Testing: Test the priority calculation using "test\_cases.py".



\## Technologies Used



\- Python 3.x

\- CSV File Handling

\- Functions

\- Lists

\- Conditional Statements

\- File Handling

\- Basic Automated Testing



\## Project Structure



Crime-Case-Analyzer/

├── main.py

├── case\_manager.py

├── analysis.py

├── data\_manager.py

├── test\_cases.py

├── cases.csv

├── README.md

└── statement.md



\## How to Run



\### Prerequisites



Make sure Python 3.x is installed on your computer.



\### Run the Project



Open Command Prompt inside the project folder and run:



py main.py



The main menu provides the following options:



1\. Add Case

2\. View Cases

3\. Search Case

4\. Update Status

5\. Delete Case

6\. Exit



\### Run the Tests



To test the priority calculation, run:



py test\_cases.py



Expected output:



Priority tests passed!



\## Priority Logic



The project uses a simple demonstration rule:



\- Evidence count 3 or more → High

\- Evidence count 2 → Medium

\- Evidence count 1 or less → Low



This rule is only for educational demonstration and does not represent a real-world investigative method.



\## Case Status



A case can have one of the following statuses:



\- Open

\- Under Investigation

\- Solved



When a case is marked as Solved, the application displays a confirmation message.



\## Sample Case



Case ID: C101

Crime: Theft

Location: City Mall

Suspect: Rahul

Evidence Count: 3

Priority: High

Status: Solved



The sample information is fictional and is used only for demonstration.



\## Testing



The "test\_cases.py" file checks whether the priority calculation returns the expected result for High, Medium, and Low priority cases.



The main application was manually tested for:



\- Case registration

\- Case viewing

\- Case searching

\- Status updating

\- Case deletion

\- Case resolution



\## Future Enhancements



\- Advanced case searching and filtering

\- User login and authentication

\- Database integration

\- Detailed case reports

\- Graphical user interface

\- More advanced case analytics



\## Author



Tanishka

