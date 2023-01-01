import csv

class department :

    def __init__(self) -> None:
        pass

    def createDept() :
        dept=[input("Enter department id:"),input("Enter department name:"),input("Enter batch id")]
        with open("database/department.csv",'a',newline='') as csvfile:
            csv_writer=csv.writer(csvfile)
            csv_writer.writerow(dept)

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
            

# def avgPerf() :

#def stats() :