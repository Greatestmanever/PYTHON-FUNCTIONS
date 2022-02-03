# using reduce() to sum numbers
from functools import reduce
def sum_all (c,d):
    return c+d
digits = [1,3,5,2,4,6,7,8,0,9,6,2]
even = list(filter(lambda z: z%2==0, digits))
double = list(map(lambda z: z+2, even))

add = reduce(sum_all, double)

print(add)

# using lambda() to sum numbers
from functools import reduce

digits = [1,3,5,2,4,6,7,8,0,9,6,2]
even = list(filter(lambda z: z%2==0, digits))
double = list(map(lambda y: y+2, even))
print(double)
add = reduce(lambda c,d: c+d, double)

print(add)