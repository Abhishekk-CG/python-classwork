# # 1.
# a=100 #global variable
# def num():
#     a=10 #local variable created
#     print(a)
# num() #function calling
# print(a) #global variable calling

# # 2.
# num=100
# def numb():
#     num+=10
#     print(num)
# numb() # it will give an error because reassignment doesnt take place inside a fn of global scope

# # 3.
# num=100
# def numb():
#     global num
#     num+=10
#     print(num)
# numb() 

# # 4.
# message="global"
# def outer():
#     message="Enclosed"
#     def inner():
#         message="Local"
#         print(message)
#     inner()
# outer()

# # 5.
# # list=[4,5,6]
# def builtfun():
#     # list=[1,2,3]
#     print(list)
#     print(list("cat"))
# builtfun()

# # 6.
# message="Global"
# def outer():
#     global message
#     message="Enclosing Edited"
#     def inner():
#         message="local"
#         print(message)
#     inner()
# outer()
# print(message)

# # 7.
# message="Global"
# def outer():
#     message="Enclosing"
#     def inner():
#         nonlocal message
#         message=message+"local"
#         print(message)
#     inner()
# outer()
# print(message)

# # 8.
# message="Global"
# def outer():
#     message="Enclosing"
#     def inner():
#         global message
#         message=message+"local"
#         print(message)
#     inner()
# outer()
# print(message)

# # # 9.
# # closure:-
# # its a concept of nested function that remembers and accesses the variable from its enclosing function's scoope even after the outer functiion's 
# # execution has already finished.
# # Example of Closure:-
# def make_counter():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# counter=make_counter()
# print(counter())
# print(counter())
# print(counter())


# # 9.
# count=1
# def increment():
#     global count
#     count+=1
#     return count
# counter=increment
# print(counter())
# print(counter())
# print(counter())