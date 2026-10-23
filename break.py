# # 35.1
# while True:
#     n=int(input("Enter a number: "))
#     if n>0:
#         print(n)
#     elif n<0:
#         continue
#     else:
#         break
# # 35.2
# numbers = [12, 5, -4, 18, 0, 25, 30]
# for number in numbers:
#     if number<0:
#         continue
#     elif number==0:
#         break
#     else:
#         print(number)
# 35.3
numbers = [12, 5, -4, 18, 0, 25, 30]
for number in numbers:
    if number==8:
        print("Number Found")
        break
else:
    print("Number not Found")