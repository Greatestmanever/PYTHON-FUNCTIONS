# import sys

# s = lambda x: list(map(sys.stdout.write, x))
# print(s(['one', 'two', 'three', 'four', 'five', 'six']))

get_tens = lambda x: int(x/10)%10
print(get_tens(558))
print(get_tens(783))