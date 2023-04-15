import random

a = [random.randint(1, 100) for _ in range(10)]#generates a list of 10 random numbers, range 1 .. 100

s = 0

for i in a:
    s += i

print(f'sum list, cycle "for", a{a} \ns='+str(s))

i = 0
n = len(a)
s = 0

while i < n:
    s += a[i]
    i += 1

print(f'sum list, cycle "while", a{a} \ns='+str(s))
