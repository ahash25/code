class student:
    marks=[]
    def getData(self,rn,name,m1,m2,m3):
        student.rn=rn
        student.name=name
        student.marks.append(m1)
        student.marks.append(m2)
        student.marks.append(m3)
    def displayData(self):
        print("roll number is :",student.rn)
        print("name is:",student.name)
        print("mark in sub 1",student.marks[0])
        print("mark in sub 2",student.marks[1])
        print("mark in sub 3",student.marks[2])
        print("marks are",student.marks)
        print("total marks are:",self.total())
        print("average marks are:",self.average())
    def total(self):
         return(student.marks[0]+student.marks[1]+student.marks[2])
        
    def average(self):
         return((student.marks[0]+student.marks[1]+student.marks[2])/3
                )
rn=int(input("enter the roll number:"))
name=input("enter the name:")
m1=int(input("enter the mark in sub 1:"))
m2=int(input("enter the mark in sub 2:"))
m3=int(input("enter the mark in sub 3:"))
s1=student()
s1.getData(rn,name,m1,m2,m3)
s1.displayData()
