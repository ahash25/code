subjects=("ds","se","db","python")
marks=[]
for i in subjects:
    temp=int(input("enter the marks of subjects[{}]:".format(i)))
    marks.append(temp)
print("total:",sum(marks))
print("average:",sum(marks)/len(subjects))
marks.clear()
