import csv
#from matplotlib import pyplot

class examination :

    def __init__(self) -> None:
        pass

    def enterMarks(*args) :
        courseId=input("Enter course ID for which marks are to be updated:")
        batches=[]
        rows=[]
        batch_marks=[]
        student_marks=""
        with open("database/batch.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                courses=row[3].split(':')
                if courseId in courses:
                    batches.append(row[0])
        with open("database/student.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[3] in batches:
                    marks=input("Enter the marks of "+row[1]+"(Student ID:"+row[0]+") :")
                    student_marks+=row[0]+":"+marks+"-"
                    batch_marks.append([row[3],row[0],courseId,marks])#batch id,student id,course id,marks
        student_marks=student_marks[:-1]
        with open("database/course.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==courseId :
                    rows.append([row[0],row[1],student_marks])
                else :
                    rows.append(row)
        with open("database/course.csv",'w',newline='') as csvfile:
            csv_writer=csv.writer(csvfile)
            if len(rows)>0:
                for row in rows:
                    csv_writer.writerow(row)
        with open("database/batch_marks.csv",'a',newline='\n') as csvfile:
            csv_writer=csv.writer(csvfile)
            for row in batch_marks:
                csv_writer.writerow(row)


    #def viewMarks() :

    #def examStats() :'''
