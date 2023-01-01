import csv

class student:
    def __init__(self) -> None:
        pass

    def createStudent(*args):# Argument should be in (student id, name , roll , batch id)
        data=list(args[1:5])
        with open("database/student.csv",'a',newline='') as csvfile :
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)


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

