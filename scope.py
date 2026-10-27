# # 1.
# a=100 #global variable
# def num():
#     a=10 #local variable created
#     print(a)
# num() #function calling
# print(a) #global variable calling

# 2.
num=100
def numb():
    num+=10
    print(num)
numb() # it will give an error because reassignment doesnt take place inside a fn of global scope

# 3.
num=100
def numb():
    global num
    num+=10
    print(num)
numb() 