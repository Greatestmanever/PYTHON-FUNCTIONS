# a = 2
# adder1 = lambda b: a + b
# # a = 3
# adder2 = lambda b: a + b

# print(adder1(1))
# print(adder2(5))

a = 5
adder1 = lambda b, a=a: a + b
a = 4
adder2 = lambda b, a=a: a + b

print(adder1(1))
print(adder2(5))
