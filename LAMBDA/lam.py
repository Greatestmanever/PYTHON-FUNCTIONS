# list1 = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

# for num in list1:
#     print(num(3))
#     print(num)

def num1(a):
    return a ** 2

def num2(a):
    return a ** 3

def num3(a):
    return a ** 4
my_list = [num1, num2, num3]

for num in my_list:
    print(num(5))


