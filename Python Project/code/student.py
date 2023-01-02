import csv
from update import update_csv

class student:
    def __init__(self) -> None:
        pass

    def createStudent(*args):# Argument should be in (student id, name , roll , batch id)
        data=list(args[1:5])
        with open("database/student.csv",'a',newline='') as csvfile :
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)
        update_csv()


    def updateStudent(*args):# Argument should be in (student id, name , roll , batch id)
        data=list(args[1:5])
        rows=[]
        with open("database/student.csv",'r') as csvfile :
            csvreader=csv.reader(csvfile)
            for row in csvreader :
                if row[0]==data[0]:
                    rows.append(data)
                else :
                    rows.append(row)
        with open("database/student.csv",'w',newline='') as csvfile :
            csvwriter=csv.writer(csvfile)
            for row in rows:
                csvwriter.writerow(row)
        update_csv()

    
    def removeStudent(*args):# Argument should be in (student id, name , roll , batch id)
        data=list(args[1:5])
        rows=[]
        with open("database/student.csv",'r') as csvfile :
            csvreader=csv.reader(csvfile)
            for row in csvreader :
                if row[0]==data[0]:
                    continue
                else :
                    rows.append(row)
        with open("database/student.csv",'w',newline='') as csvfile :
            csvwriter=csv.writer(csvfile)
            for row in rows:
                csvwriter.writerow(row)
        update_csv()
    
    def grade(*args):
        marks=args[1]
        if marks>=90:
            return 'A'
        elif marks>=80:
            return 'B'
        elif marks>=70:
            return 'C'
        elif marks>=60:
            return 'D'
        elif marks>=50:
            return 'E'
        else :
            return 'F'

    def genReport(*args):
        s=student()        
        student_id=input("Enter a student ID:")
        with open("database/student.csv") as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if student_id==row[0]:
                    data=row
                    break;
        dict_grades={}
        dict_courses={}
        courses=[]
        with open("database/batch_marks.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[1]==student_id:
                    dict_grades[row[2]]=s.grade(int(row[3]))
                    courses.append(row[2])
        with open("database/course.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0] in courses:
                    dict_courses[row[0]]=row[1]
        with open("text/report.txt",'w+') as file:
            file.write("REPORT")
            file.write("\n"*3)
            file.write("Name:"+data[1]+(" "*(30-len(data[1])-len("Name:")))+"Roll No.:"+data[2]+"\n")
            file.write("Batch ID:"+data[3]+(" "*(30-len(data[3])-len("Batch ID:")))+"Student ID:"+data[0])
            file.write("\n"*3)
            for course in courses:
                file.write("Course Name:"+dict_courses[course]+(" "*(30-len(dict_courses[course])))+"Grade:"+dict_grades[course]+"\n")
