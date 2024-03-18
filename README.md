3005Assignment3Question1

Database Interaction with PostgreSQL & Python
It is a Python application designed to interact with a PostgreSQL database for managing student records. It supports basic CRUD 

Zainab Lezzaik - 101263105

REQUIREMENTS : 
Ensure you have the following installed

Python 3.x
PostgreSQL
Application Set up
Clone Repo to local machine


Install psycopg2 from the terminal
pip3 install psycopg2

Database Set up
Create and name a database using pgAdmin (or PostgreSQL command line)
In the browser panel on the left, right-click on Databases and select Create > Database
Name the new database "schoolDatabase" and click Save (Note you can name whatever you want)
Run the SQL commands in the q1db.sql to set up database schema and insert initial data

Right-click on the database name in pgAdmin4 : 
Choose Query Tool to open an SQL editor window.
In the Query Tool, click on the Open File button and choose the q1db.sql file in the database directory
Once the file is open in the editor, click on the green Run button to execute the SQL commands

Running the Application : 
Run the applicationFunctions file using this command :  python3 applicationFunctions.py

Link to the Video : https://youtu.be/vp_e8fmHEmg 
