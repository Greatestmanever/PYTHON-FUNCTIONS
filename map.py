# #without using map

# lis = [10,9,8,7,6,5,4,3,2,1]

# def func(a):
#     return a**a

# newlist = []
# for a in lis:
#     newlist.append(func(a))

# print(newlist)

# #using map() function

# lis = [10,9,8,7,6,5,4,3,2,1]

# def func(a):
#     return a**a

# print(list(map(func,lis)))

#using list comprehension function

lis = [10,9,8,7,6,5,4,3,2,1]

def func(a):
    return a**a

print([func(a) for a in lis])

print([func(a) for a in lis if a%2==0])