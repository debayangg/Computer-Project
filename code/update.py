import csv
import pandas as pd

def update_csv():
    #update batch when student is changed
    dict_stud={}
    with open("database/student.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            dict_stud[row[3]]=""
        csvfile.seek(0)
        next(csvreader)
        for row in csvreader:
            dict_stud[row[3]]+=row[0]+":"
    batch=pd.read_csv("database/batch.csv")
    count=0
    for i in batch['Batch_ID']:
        batch.List_of_Students[count]=dict_stud[i][:-1]
        count+=1
    batch.to_csv("database/batch.csv",index=False)

    #change department when batch is changed
    dict_batch={}
    with open("database/batch.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            dict_batch[row[2]]=""
        csvfile.seek(0)
        next(csvreader)
        for row in csvreader:
            dict_batch[row[2]]+=row[0]+":"
    dept=pd.read_csv("database/department.csv")
    count=0
    for i in dept['Department_ID']:
        dept.List_of_Batches[count]=dict_batch[i][:-1]
        count+=1
    dept.to_csv("database/department.csv",index=False)

