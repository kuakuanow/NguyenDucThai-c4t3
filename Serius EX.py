# SERIUS EX:
# 1
# x = int(input("Chiều cao cơ thể (cm)? "))
# y = int(input("Cân nặng cơ thể (kg)? "))
# bmi= (y/((x*x)/10000))
# if bmi<16:
#     print("Bạn nên tăng cân mạnh")
# elif bmi <= 18.5:
#     print ("Bạn nên tăng cân")
# elif bmi<=25:
#     print("Your good!")
# elif bmi <= 30:
#     print ("bạn bị thừa cân")
# else:
#     print ("Bạn bị béo phì")


# # 2
# n = int(input ("Điền giai thừa:"))
# if n == 0:
#     print("0! = 1")
# elif n < 0:
#     print("Error input! Please Re-Run the program.")
# else:
#     s = 1
#     for i in range(1, n+1):
#         s = s * i
#         i = i + 1
#     print(s)


# 3

# 3.a.1
# for i in range(0, 20):
#     print(i, end=(' '))

# 3.a.2
# n = int(input("Enter the number: "))
# if n < 0:
#     print("You must enter the positive numbers! Please Re-run program.")
# else:
#     for i in range(0, n):
#         print(i, end=(' '))

# 3.b.1
# n = 20
# a = 0
# for i in range(n):
#     if a == 1:
#         a = a - 1
#     elif a == 0:
#         a = a + 1
#     print(a, end=' ')

# 3.b.2
# n = int(input("Enter the total number of 1's and 0's in total consecutively: "))
# a = 0
# if n < 0:
#     print("You must enter the positive numbers! Please Re-run program.")
# else:
#     for i in range(n):
#         if a == 1:
#             a = a - 1
#         elif a == 0:
#             a = a + 1
#         print(a, end=' ')

