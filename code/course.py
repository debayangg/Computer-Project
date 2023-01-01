import csv
from matplotlib import pyplot as plt
import student
#import pandas as pd
#import numpy as np

class course :

    def __init__(self) -> None:
        pass

    def createCourse(*args) :
        data=list(args[1:3])#only initialise the course name and id
        with open("database/course.csv",'a',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow([
                data[0],
                data[1],
                data[2] if data[2] else "" 
            ])


    def studentPerf(*args) :
        #display the names of all students, info and the repective marks
        course_id=input("Enter the course ID:")
        students=[]
        student_ids=[]
        student_marks=[]
        with open("database/course.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==course_id:
                    students=row[2].split('-')
                    break
        for i in students:
            #student_ids.append(i[:i.find(":")])
            #student_marks.append(i[i.find(":"):])
            with open("database/student.csv",'r') as csvfile:
                csv_reader=csv.reader(csvfile)
                for row in csv_reader:
                    if row[0]==i[:i.find(":")]:
                        print("Name:",row[1],"\t\tStudent ID:",row[0],"\tRoll No.:",row[2],"\tMarks:",i[i.find(':'):])



    def courseStat(*args) :
        student1=student.student()
        marks=[]
        courseID=input("Enter the course ID:")
        with open("database/course.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==courseID:
                    s=row[2].split('-')
        for row in s:
            grade=student1.grade(int(row[row.find(':'):]))
            marks.append(grade)
        plt.hist(marks,bins=['A','B','C','D','E','F'])
        plt.xlabel('Grades')
        plt.ylabel('No. of Students')
        plt.title('Marks Distribution'+courseID)

c=course()
c.courseStat()