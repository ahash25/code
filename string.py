str="a string"
print("the original string is:",str)
reverse_string=" "
count=len(str)
while count>0:
    reverse_string+=str[count-1]
    count=count-1
print("the reversed string using a while loop is:",reverse_string)    
