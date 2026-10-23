# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# i=1
# while i!=0:
#     print("""Enter your choice:
# 1 for addition
# 2 for subtraction
# 3 for multiplication
# 4 for division""")
#     operation=int(input("Enter your choice: "))
#     match operation:
#         case 1:
#             print("Addition")
#             print(f"Addition of {a} and {b} is {a+b}")
#         case 2:
#             print("Subtraction")
#             print(f"Subtraction of {a} and {b} is {a-b}")
#         case 3:
#             print("Multiplication")
#             print(f"Multiplication of {a} and {b} is {a*b}")
#         case 4:
#             print("Division")
#             if b!=0:
#                 print(f"Division of {a} and {b} is {a/b}")
#             else:
#                 print("Division by zero is not allowed.")
#             break
#         case _:
#             print("Invalid choice. Please enter a valid option.")
#     print("To break the loop enter 0, to continue enter any other number.")
#     i=int(input("Enter your choice for loop: "))
#     if i==0:
#         print("Loop ended.")
# # 2.
# day=int(input("Enter a daycode: "))
# match day:
#     case 1|2|3|4|5:
#         print("Working Day")
#     case 6|7:
#         print("Weekend")
# # 3.
# marks=int(input("Enter your marks: "))
# match marks:
#     case x if x>=90:
#         print("A")
#     case x if x>=80:
#         print("B")
#     case x if x>=70:
#         print("C")
#     case x if x>=60:
#         print("D")
#     case x if x>=50:
#         print("E")
#     case x if x<=40:
#         print("FAIL")
#     case _:
#         print("Enter a valid marks")
# # 4.
# account=input("Enter your Designantion: ").lower()
# if account=="student":
#     print("""Enter 
# 1 for Courses
# 2 for Marks
# 3 for Attendance
# """)
# elif account=="teacher":
#     print("""Enter 
#     1 for Student list
#     2 for Marks
#     3 for timetable""")
# choice=int(input("Enter your choice: "))
# match account:
#     case "student":
#         match choice:
#             case 1:
#                 print("You are enrlled in B.tech")
#             case 2:
#                 print("You have got 98 marks.")
#             case 3:
#                 print("you have maintaineed 100 percentage of attendance.")
#             case _:
#                 print("Invalid choice")
#     case "teacher":
#         match choice:
#             case 1:
#                 print("The total number of students are 89.")
#             case 2:
#                 print("This student has got 89 marks.")
#             case 3:
#                 print("Your class is scheduled in lab4.")
#             case _:
#                 print("Invalid choice")
#     case _:
#         print("Invalid Account Type")
# # 5.
# str=input("Enter a string: ").lower()
# length=len(str)
# for i in range(length):
#     char=str[i]
#     if char=="o":
#         print("Found")
# # 6.
# str=input("Enter a string: ").lower()
# flag=False
# for i in str:
#     if "o" in str and flag==False:
#         flag=True
#         print("Found")
# if not flag:
#     print("Not found")
# # 7.
# for i in range(3):
#     for j in range(3):
#         break
#     print(i)
#     break
# # 8.
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)
# # 9.
# numbers = [10, 20, 30, 40, 50]
# n=len(numbers)
# for i in range(n):
#     num=numbers[i]
#     if num==30:
#         print("Found")
#         break
# # 10.
# i=int(input("Enter a number: "))
# while i!=0:
#     i=int(input("Enter a number: "))
#     if i==0:
#         break
# # 11.
# flag=False
# while flag==False:
#     num=int(input("Enter a number: "))
#     if num==0:
#         flag=True
#         break
# # 12.
# for i in range(1,100):
#     if i%17==0:
#         break
#     print(i)
# # 13.
# i=True
# while i==True:
#     num=int(input("Enter a number: "))
#     if num==0:
#         break
# 14.
