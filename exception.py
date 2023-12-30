def divide(num,den):
    res=num/den
    return res
try:
    num=int(input("enter the numerator:"))
    den=int(input("enter the denominator:"))
    result=divide(num,den)
    print("result=",result)
except valueError:
    print("main block:invalid input")
except zeroDivisionError:
    print("main block:divide by zero error")
print("end of program")    
