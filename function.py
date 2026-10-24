# # 1.
# def calculator():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter second number: "))
#     print("""Enter
#     1 for addition
#     2 for subtraction
#     3 for multiplication
#     4 for division
#     5 for floor division
#     6 for exponentiation
#     7 for modulus""")
#     n=int(input("Enter a number for mathematical calculation: "))
#     if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7:
#         if n==1:
#             calc=a+b
#             print(f"Your result for the addition of numbers {a} + {b} = {calc}")
#         if n==2:
#             calc=a-b
#             print(f"Your result for the subtraction of numbers {a} - {b} = {calc}")
#         if n==3:
#             calc=a*b
#             print(f"Your result for the multiplication of numbers {a} * {b} = {calc}")
#         if n==4:
#             calc=a/b
#             print(f"Your result for the division of numbers {a} / {b} = {calc}")
#         if n==5:
#             calc=a//b
#             print(f"Your result for the floor division of numbers {a} // {b} = {calc}")
#         if n==6:
#             calc=a**b
#             print(f"Your result for the exponentiation of numbers {a} ** {b} = {calc}")
#         if n==7:
#             calc=a%b
#             print(f"Your result for the modulus of numbers {a} % {b} = {calc}")
#     else:
#         print("Invalid input for mathematic calculation.")
# calculator()

# # 2.
# bal=30000
# def bank_fn(credit_bal,withdraw_amt):
#     avl=bal
#     avl+=credit_bal
#     print("""
# Your Amount credited successfully! Available Balance: """,avl)
#     avl-=withdraw_amt
#     print("""
# Amount debited successfully! Available Balance: """,avl)

# bank_fn(2000,5000)

# # 3.
# a=10
# b=20
# c=30
# def product(a,b):
#     c=a*b
#     return c

# def sub(a,b):
#     c=a-b
#     return c

# def add(a,b):
#     c=a+b
#     return c

# print(product(add(sub(a,b),c),c))

# # 4.
# def calculate(a,b):
#     total=a+b
#     diff=a-b
#     return total,diff
# print(calculate(8,9))  #this creates the result in the form of tuple.
# add,difference=calculate(8,9)
# print(add,difference)  #This is the way we can unpack tuple.
# # 5.
# def greet(name="Guest"):
#     print("Hello", name)

# print(greet())
# greet("Asha")

# # 6.
# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Asha")

# # 7.
# def print_val(name, job, age=22,):
#     print(name,age,job)
# print_val("yono",23,"magic knight")

# # 8.
# def Myfunction():
#     return "Catch me if you can!"
# print(Myfunction())
# print("Done")

# # 9.
# def stop():
#     return
# print(stop())

# # 10.
# def one_value():
#     return 10
# def two_value():
#     return 10,20
# print(one_value())
# print(two_value())

# # 11.
# def subtract(a, b):
#     return a - b

# print(subtract(8, 3))
# print(subtract(3, 8))

# # 12.
# def calculate(number):
#     return number * 2

# result = calculate(5)
# print(result + 3)

# # 13.
# def greet(name="Guest"):
#     return "Hello " + name

# print(greet())
# print(greet("Asha"))

# # 14.
# def values():
#     return 10, 20

# a, b = values()
# print(a + b)

# # 15.
# fact=1
# def counter_fun(count):
#     global fact
#     fact*=count
#     count-=1
#     if(count==1): 
#         return fact
#     if count==0:
#         return 1
#     return counter_fun(count)
# print(counter_fun(19))

# # 16.
# def divide(c,*args,d=20,**kwargs):
#     print(type(args))
#     print(type(kwargs))
#     return args,kwargs,c+d
# print(divide(14,15,2,32,52,p=67,q=89,r="Apple"))

# # 17.
# print(type((3,)))

# # 18.
# def add(a,b,c):
#     return a+b+c
# number={"a":10,"b":20,"c":30}
# print(add(**number))
# number={"p":10,"q":20,"r":30}
# print(add(**number))

# 19.
def show_letters(a,b,c):
    print(a,b,c)
show_letters(*"cat")