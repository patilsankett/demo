""" 
int (input("Enter Your number"))
print(type(a))
b =10
c=a+b
print("this is a+b",c) 
print(f"this is {a}")

20>10 
"""
# Program to check if number is odd or even return true if odd
"""
a=int (input("number"))
print(f"{a} is odd is ",a%2==1)
print(f"{a} is odd is ",a%2!=0)
"""
#Program to print age in days
"""
age=int(input("Age:"))
b=age*365
print(f"{age} years = {b} days")
print(age,"years=",b,"days")
"""
#convert minutes into hours 
"""
minutes=int(input("enter"))
b=minutes%60
print(minutes,"=",minutes//60,"hour",b,"minutes")
"""

#program to extract last digit of a number 
"""
a=int(input("Enter the Number"))
b=a%10
print(a,": last digit is",b)
"""

#program to check if person is student or teacher with age below 21

"""
age=int(input("Enter Your Age : "))
role=input("Are You Teacher or Student : ")
print("Eligible :",age<=21)
"""

#Program to swap two variable without a third variable using arithmetic operations 



#if else statement 
"""
is_raining=False
if is_raining:
 print("Raining Outside")
else:
 print("Not Raining Outside")
 """

#eligible to vote above 18
"""
age=int(input("Enter Your Age :"))
if age>=18:
    print("Eligible to Vote")
else:
    print("Not Eligle to Vote")
"""
#if el
"""
num=int(input("Enter Your Number :"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:    
    print("Wednesday")  
elif num==4:    
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid Input")
"""

#nested loop
"""
age=int(input("Enter Your Age :"))
has_id=True
if age>=18:
    if has_id:
        print("Valid Id")
    else:
        print("Id Invalid")
else:
    print("Underage")
"""

#match case statement
"""
day=int(input("Enter Your Day number:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
        """

#odd or even using elif

num=int(input("Enter the Number :"))