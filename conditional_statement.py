# #1.
# age=(input("enter your age: ").split()[0:1])
# age=int(age[0])
# print(age)
# age1=int(age)
# gender=input("Enter your gender: ")
# gender=gender.strip().lower()
# print(age,gender)
# if age>=18:
#     if gender=="female":
#         print("The seat is available for you")
#     else:
#         print("The seat isn't available for you")
# #2.
# username=input("Enter your Username: ").lower()
# password=input("Enter your Password: ")
# if username == codinggita@gmail.com:
#     if password == 12345:
#     else:
#         print("Your password is incorrect")
# else:
#     print("your Username is incorrect")
# #3.
# print("'press the number for specific operations" \
# "       1. For Addition" \
# "       2. For Subtraction" \
# "       3. For Multiplication" \
# "       4. For Division" \
# "       5. For Floor division'")
# first=int(input("Enter first Number: "))
# second=int(input("Enter second Number: "))
# operation=int(input("Enter the Number for operation: "))
# if operation==1:
#     print(first+second)
# elif operation==2:
#     print(first-second)
# elif operation==3:
#     print(first*second)
# elif operation==4:
#     print(first/second)
# elif operation==5:
#     print(first//second)
# else:
#     print("Error!!! Please specify the operation number from Menu bar")
# #4.
# x=int(input("Enter a three digit number: "))
# y=(x%10)
# a=(x//10)
# z=a//10
# print(f"The sum of all the 3 digit is {(y)+(a%10)+(z%10)}.")
# #5.
# for i in range (1,20):
#     if i%2==0:
#         print(f"{i} is even no.")
# #6.
# num=int(input("Enter a Four digit number: "))
# sum=0
# sum=sum+num%10
# num=num//10
# for i in range ()
# #7.
# str=input("Enter a word: ").strip()
# str1=(str.lower())
# str2=""
# length=len(str1)
# for i in range((length-1),-1,-1):
#     str2=str2+str1[i]
# if str==str2:
#     print("Its a pallindrome string")
# else:
#     print("Its not a pallindrome string")
# #8.
# name=input("Enter a string: ")
# length=len(name)
# for i in range(length):
#     print(name[i])
# #9.
# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()
# #10.
# for i in range(4):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# #11.
# for i in range(1,5):
#     print(i*"*")
# #12.
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
# #13.
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# #14.
# x=int(input("Enter a number: "))
# for row in range(1,x+1):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()
# #15.
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()
# #16.
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()
# #17.
# for i in range(1,6):
#     for k in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,6-i):
#         print("*",end="")
#     print()
#19.
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(" ",end="")
#     for k in range(1,n+2-i):
#         print("*",end="")
#     print()
# #20.
# for i in range(1,7):
#     x=(2*i-1)
#     for j in range(1,7-i):
#         print(" ",end="")
#     for k in range(1,x+1):
#         print("*",end="")
#     print()
# #21.
# n=int(input("Enter a number: "))
# for row in range(1,n+1):
#     for col in range(1,n-row+1):
#         print(" ",end="")
#     for pyr in range(1,2*row):
#         print("*",end="")
#     print()
# #22.
# total=0
# grade=""
# flag=True
# for i in range(5):
#     marks=int(input("Enter your marks: "))
#     total=total+marks
#     if marks<35:
#         flag=False

# percentage=total/5

# if flag==True:
#     if percentage>=90:
#         grade="A+"
#     elif percentage>=80:
#         grade="A"
#     elif percentage>=70:
#         grade="B"
#     elif percentage>=60:
#         grade="C"
#     elif percentage>=50:
#         grade="D"
#     else:
#         grade="F"
        
# num=0
# while num==5:
#     print("Apple")

# #23.
# for row in range(5):
#     for col in range(5):
#         if (col==0 or col==4 or row==4) or (col==2 and row==2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #24.
# n=int(input("Enter the range: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# for k in range(n-1,0,-1):
#     for l in range(1,k+1):
#         print(l,end="")
#     print()
# #25.
# i=1
# while i<=5:
#     print("Hello world")
#     i+=1