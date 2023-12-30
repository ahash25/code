rollno=set()
flag=1
while flag:
    temp=input("enter the rollno of the student")
    rollno.add(temp)
    chk=int(input("press 1 to add more"))
    if(chk!=1):
        flag=0
        print("entered roll number are",rollno)
        course={}
name=input("enter course name:")
course.update({"name":name})
duration=input("enter the course duration:")
course.update({"duration":duration})
course.update({"student":rollno})
print(course)
