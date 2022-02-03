# functions to display even number using filter()

def even_no(z):
    return z % 2==0
digits = [1,3,5,2,4,6,7,8,0,9,6,2]
even = list(filter(even_no,digits))
print(even)

# functions to display even number using lambda()

digits = [1,3,5,2,4,6,7,8,0,9,6,2]
even = list(filter(lambda z :z % 2==0,digits))
print(even)

# functions to double the even number even number using map()

digits = [1,3,5,2,4,6,7,8,0,9,6,2]
even = list(filter(lambda z: z%2==0, digits))
double = list(map(lambda z: z+2, even))
power_of_no = list(map(lambda a: a*2, even))
print(double)
print(power_of_no)