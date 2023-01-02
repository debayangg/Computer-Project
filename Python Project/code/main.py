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
        "4.Department\n",
        "5.Examination")
option=int(input("Enter your choice:"))

if option==1 :

    os.system('clear')
    new_student=student.student()
    print("Choose an option:\n",
          "1.Create a new student\n",
          "2.Update a students details in the database\n",
          "3.Remove a students details from database\n",
          "4.Print a report")
    option1=int(input("Enter your choice:"))
    
    if option1==1 :
        # Argument should be in (student id, name , roll , batch id)
        os.system('clear')
        data=[]
        data.append(input("Enter student id:"))
        data.append(input("Enter student's name:"))
        data.append(input("Enter student's roll number:"))
        data.append(input("Enter student's batch id:"))
        new_student.createStudent(data[0],data[1],data[2],data[3])
    
    elif option1==2 :
        os.system('clear')
        new_student.updateStudent(
            input("Enter student id:"),
            input("Enter student's name:"),
            input("Enter student's roll number:"),
            input("Enter student's batch id:"),
        )

    elif option1==3 :
        os.system('clear')
        new_student.removeStudent(
            input("Enter student id:"),
            input("Enter student's name:"),
            input("Enter student's roll number:"),
            input("Enter student's batch id:"),
        )

    elif option1==4:
        new_student.genReport()

    else :
        print("Option not found")

elif option==2:
    
    os.system('clear')
    new_course=course.course()
    print("Choose an option:\n",
          "1.Create a course\n",
          "2.Show the students and their details in a course\n",
          "3.Display histogram representing the marks of students")
    option2=int(input("Enter your choice:"))

    if option2==1:
        os.system('clear')
        new_course.createCourse()
    
    elif option2==2:
        os.system('clear')
        new_course.studentPerf()

    elif option2==3:
        os.system('clear')
        new_course.courseStat()

    else :
        os.system('clear')
        print("Option not found")

elif option==3:
    
    os.system('clear')
    new_batch=batch.batch()
    print("Choose an option:\n",
          "1.Create a new batch\n",
          "2.View students in a batch\n",
          "3.View courses in a batch\n",
          "4.View student performance in a batch\n"
          "5.Pie Chart to view makes of the students as a percentage")
    option3=int(input("Enter your choice:"))

    if option3==1:
        os.system('clear')
        new_batch.createBatch()

    elif option3==2:
        os.system('clear')
        new_batch.viewStudent()

    elif option3==3:
        os.system('clear')
        new_batch.viewCourse()

    elif option3==4:
        os.system('clear')
        new_batch.studentPerf()

    elif option3==5:
        os.system('clear')
        new_batch.studentPercen()

    else:
        os.system('clear')
        print("Option does not exist")
    
elif option==4:
    
    os.system('clear')
    new_dept=department.department()
    print("Choose an option:\n",
          "1.Create a new department\n",
          "2.View batch in a department\n",
          "3.View performance of students in a a department\n",
          "4.Line plot of batch percentages")
    option3=int(input("Enter your choice:"))

    if option3==1:
        os.system('clear')
        new_dept.createDept()

    elif option3==2:
        os.system('clear')
        new_dept.viewBatch()

    elif option3==3:
        os.system('clear')
        new_dept.avgPerf()

    elif option3==4:
        os.system('clear')
        new_dept.stats()

    else:
        os.system('clear')
        print("Option does not exist")

elif option==5:

    os.system('clear')
    new_exam=examination.examination()
    print("Choose an option:\n",
          "1.Enter their marks\n",
          "2.View marks of a particular course\n",
          "3.Scatter plot for dept")
    option3=int(input("Enter your choice:"))

    if option3==1:
        os.system('clear')
        new_exam.enterMarks()

    elif option3==2:
        os.system('clear')
        new_exam.viewMarks()

    elif option3==3:
        os.system('clear')
        new_exam.examStats()

    else:
        os.system('clear')
        print("Option does not exist")