import csv

class batch :
    def __init__(self) -> None:
        pass

    def createBatch(*args) :
        batch_id=input("Enter the batch id:")
        batch_name=input("Enter the batch name:")
        course_id=""
        print("Select department:")
        with open("database/department.csv",'r') as csvfile:
            csv_read=csv.reader(csvfile)
            for row in csv_read:
                print(row[0])
        dept_id=input("Enter the department id:")
        print("Select courses to add to this batch:")
        flag=True
        while(flag):
            with open("database/course.csv",'r') as csvfile:
                csv_read=csv.reader(csvfile)
                next(csv_read)
                for row in csv_read:
                    print("Course Name:",row[1],"(Course ID:",row[0],")")
                print("Type 0 to stop course input")
                course_input=input("Enter the course ID:")
                if course_input=='0' :
                    flag=False
                else:
                    course_id=course_id+course_input+":"
        course_id=course_id[:-1]
        data=[batch_id,batch_name,dept_id,course_id,""]
        with open("database/batch.csv",'a',newline='\n') as csvfile:
            csv_writer=csv.writer(csvfile)
            csv_writer.writerow(data)


    def viewStudent(*args) :
        batch_id=input("Enter the batch id:")
        students=[]
        with open("database/batch.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==batch_id:
                    students=row[4].split(':')
                    break
        print("The students in",batch_id,":")
        with open("database/student.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0] in students:
                    print("Name: "+row[1]+" ,Student ID: "+row[0])
        


    def viewCourse(*args) :
        batch_id=input("Enter the batch id:")
        courses=[]
        with open("database/batch.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==batch_id:
                    courses=row[3].split(':')
                    break
        print("The courses in",batch_id,":")
        with open("database/course.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0] in courses:
                    print("Name: "+row[1]+" ,Course ID: "+row[0])


    def studentPerf(*args) :
        batch_id=input("Enter a batch ID:")
        dict_marks={}
        with open("database/batch_marks.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==batch_id and not( row[1] in dict_marks.keys()) :
                    student_id=row[1]
                    dict_marks[student_id]=0
                    marks=0
                    subjects=0
                    with open("database/batch_marks.csv",'r') as csvfile1:
                        csv_reader1=csv.reader(csvfile1)
                        for row1 in csv_reader1:
                            if row1[1]==student_id:
                                marks+=int(row1[3])
                                subjects+=1
                    dict_marks[student_id]=(marks/subjects)
        with open("database/student.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[3]==batch_id :
                    print("Name:",row[1],"\tStudent ID:",row[0],"\tRoll No.:",row[2],"\tMarks:",dict_marks[row[0]])
    
    
    #def studentPercen() :

check=batch()
check.studentPerf()