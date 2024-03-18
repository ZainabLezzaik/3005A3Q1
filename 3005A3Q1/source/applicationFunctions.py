#this is importing the get_DB_connection function from the connetToDb file
from connectToDb import get_DB_connection

def getAllStudents() : 
    connect = get_DB_connection()
    cur = connect.cursor()
    cur.execute('SELECT * FROM students')
    stu = cur.fetchall()
    for student in stu:
        print(student)
    cur.close()
    connect.close()


def addStudent(first_name, last_name, email, enrollment_date):
    connect = get_DB_connection()
    cur = connect.cursor()
    # this will check if the email of the student we're trying to add exists
    cur.execute("SELECT * FROM students WHERE email = %s", (email,))
    if cur.fetchone() is not None:
      # if it does, then print the statement below and return nothing
      print("THIS Email already exists !")
      return
    #if the email does not exist, then we add the student
    cur.execute('INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)',
                (first_name, last_name, email, enrollment_date))
    connect.commit()
    cur.close()
    connect.close()



def updateStudentEmail(student_id, new_email):
    connect = get_DB_connection()
    cur = connect.cursor()

      #this checks if the new email already exists in the database
    cur.execute("SELECT * FROM students WHERE email = %s", (new_email,))
    if cur.fetchone() is not None:
      print("This new email already exists! Please use a DIFFERENT email !")
      return
    # if it does not, then get the student with the specified id and change its email
    cur.execute('UPDATE students SET email = %s WHERE student_id = %s',
                (new_email, student_id))
    connect.commit()
    cur.close()
    connect.close()



def deleteStudent(student_id):
    connect = get_DB_connection()
    cur = connect.cursor()
    #this will first check if the student_id we specified exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    if cur.fetchone() is None:
        # if it does not, then return nothing and print this statement
        print("Student with this ID DOESN'T exist")
        return
    # if it does, then delete the student with the specified stundet_id
    cur.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
    connect.commit()
    cur.close()
    connect.close()


def main():
  #this will show all the students in the school
  print("All the students in this database : ")
  getAllStudents() 

   #this will add a student to the database
  print("\n Adding student Zainab to the database:")
  addStudent("Zainab", "Lezzaik", "zlezzaik@carleton.ca", "2023-9-3")
  print("\n All the students in this database after adding Zainab : ")
  getAllStudents() 

   #this will update the email for student with student_id 1
  print("\n Updating the email for student with student_id 1")
  updateStudentEmail(1, "john_NEW_email@example.com")
  print("\n All the students in this database after updating the email for student with student_id 1: ")
  getAllStudents() 

  #this will delete the student with student_id 2
  print("\n Deleting the student with student_id 2")
  deleteStudent(2)
  print("\n All the students in this database after deleting the student with student_id 2: ")
  getAllStudents() 

main()