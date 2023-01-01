import student
import course
import batch
import examination
import department
import os

print("STUDENT MANAGEMENT SYSTEM")
print('\n'*5)
print("Choose an option:\n",
        "1.Student\n",
        "2.Course\n",
        "3.Batch\n",
        "4.Course\n",
        "5.Department\n",
        "6.Examination")
option=int(input("Enter your choice:"))

if option==1 :
    os.system('cls')
    new_student=student.student()
    print("Choose an option:\n",
          "1.Create a new student\n",
          "2.Update a students details in the database\n",
          "3.Remove a students details from database\n",
          "4.Print a report")
    option1=int(input("Enter your choice:"))
    
    if option1==1 :
        # Argument should be in (student id, name , roll , batch id)
        os.system('cls')
        data=[]
        data.append(input("Enter student id:"))
        data.append(input("Enter student's name:"))
        data.append(input("Enter student's roll number:"))
        data.append(input("Enter student's batch id:"))
        new_student.createStudent(data[0],data[1],data[2],data[3])
    
    elif option1==2 :
        os.system('cls')
        new_student.updateStudent(
            input("Enter student id:"),
            input("Enter student's name:"),
            input("Enter student's roll number:"),
            input("Enter student's batch id:"),
        )

    elif option1==3 :
        os.system('cls')
        new_student.removeStudent(
            input("Enter student id:"),
            input("Enter student's name:"),
            input("Enter student's roll number:"),
            input("Enter student's batch id:"),
        )

    else :
        print("Option not found")

