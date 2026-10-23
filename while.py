# #1.
# i=1
# while i<=10:
#     print(i*2)
#     i+=1
# #2.
# num=int(input("Enter a Number: "))
# while num!=0:
#     print("Invalid Input")
#     num=int(input("Enter a number: "))
# print("Loop ended")
# #3.
# str=input("Enter a string: ").strip()
# str=str.lower()
# length=len(str)
# i=length-1
# str1=""
# while i>=0:
#     char=str[i]
#     str1+=char
#     i-=1
# if str1==str:
#     print("Its a pallindrome")
# else:
#     print("Its not a pallindrome")
# #4.
# str1=input("Enter a pallindrome string: ").strip()
# length=len(str1.lower())
# flag=True
# i=0
# j=length-1
# while i<j:
#     if str1[i]==str1[j]:
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j #To break the loop.
# if flag:
#     print("Its a pallindrome.")
# else:
#     print("Not a pallindrome.")
# # 5.
# number=int(input("Enter a number: "))
# while number>0:
#     digit=number%10
#     print(digit)
#     number//=10
# # 6.
# age=int(input("Enter your age: "))
# while age<0:
#     print("Age cant be negative.")
#     age=int(input("Enter your age again: "))
# print(f"Your age is {age} years.")
# # 7.
# total=0
# numb=int(input("Enter your number: "))
# while numb>0:
#     digit=numb%10
#     print(digit)
#     total+=digit
#     numb//=10
# print(f"The sum of the digits are {total}")
# # 8.
# x=int(input("Enter a number: "))
# while x<0:
#     print("Invalid Input")
#     x=int(input("Enter a number: "))
# # 9.
# count=0
# y=int(input("Enter a number: "))
# while y!=0:
#     print("Invalid Input")
#     y=int(input("Enter a number: "))
#     count+=1
# print(f"The total number of mistakes are {count}.")
# 10.
n=int(input("Enter the range for loop iteration: "))
i=1
while i<=n:
    print(i)
    i+=1