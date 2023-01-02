import csv
from matplotlib import pyplot as plt
from update import update_csv

class department :

    def __init__(self) -> None:
        pass

    def createDept() :
        dept=[input("Enter department id:"),input("Enter department name:"),input("Enter batch id")]
        with open("database/department.csv",'a',newline='') as csvfile:
            csv_writer=csv.writer(csvfile)
            csv_writer.writerow(dept)
        update_csv()

    def viewBatch() :
        dept_batch=[]
        dept_id=input("Enter the department id:")
        with open("database/department.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==dept_id:
                    dept_batch=row[2].split(':')
        print("List of batches in",dept_id,"are :")
        for i in dept_batch:
            print(i)
            
    def avgPerf(*args) :
        dept_batch=[]
        batches=[]

        dept_id=input("Enter the department id:")
        with open("database/department.csv",'r') as csvfile:
            csv_reader=csv.reader(csvfile)
            for row in csv_reader:
                if row[0]==dept_id:
                    batches=row[2].split(':')
                    break
        for batch in batches:
            flag=0
            marks=0
            with open("database/batch_marks.csv",'r') as csvfile:
                csv_reader=csv.reader(csvfile)
                for row in csv_reader:
                    print(row[0]," ",batch)
                    if row[0] == batch :
                        marks+=int(row[3])
                        flag+=1
                if(flag==0): continue
                print("Batch ID:",batch,"\tAverage Marks:",(marks/flag))

    def stats(*args) : #Line plot – Average percentage of all students for each batch. X axis - Batch Name, Y axis – Average Percentage
        dict_batches={}
        with open("database/batch_marks.csv",'r') as csvfile:
                csv_reader=csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    if not(row[0] in dict_batches.keys()):
                        batch_id=row[0]
                        dict_batches[batch_id]=0
                        with open("database/batch_marks.csv",'r') as csvfile1:
                            csv_reader1=csv.reader(csvfile1)
                            next(csv_reader1)
                            subs=0
                            for row1 in csv_reader1:
                                if batch_id==row1[0]:
                                    dict_batches[batch_id]+=int(row1[3])
                                    subs+=1
                            if subs>0:
                                dict_batches[batch_id]=dict_batches[batch_id]/subs
        plt.plot(dict_batches.keys(),list(dict_batches.values()),linestyle='--')
        plt.xlabel('Batch Percentage')
        plt.ylabel('Batch')
        plt.show()
