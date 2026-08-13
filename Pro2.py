import json
import pandas as pd

user=int(input("Enter student number= "))

Students=[]

for i in range(user):
    print("Enter details of Student:",i+1)

    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    cource=input("Enter cource name:")

    students={
    "name":name,
    "age":age,
    "cource":cource
    }



Students.append(students)

with open("Students.json","w") as file:
    json.dump(Students,file,indent=3)

with open("Students.json","r")as file:
    data=json.load(file)
print(data)

#Pandas DataFrame
df=pd.DataFrame(data)

#First two student
print("First Two Student:")
print(df.head(2))

#Last two student
print("Last Two Student:")
print(df.tail(2))

#Shap
rows,columns=df.shape
print(f"student row:{rows}")
print(f"student columns:{columns}")


#list
columns_list=list(df.columns)
print(f"column name:{columns_list}")

#data type
df=pd.DataFrame(Students)
print(f"Data type:{df.dtypes}")


