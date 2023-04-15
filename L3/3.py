# divisors of a number


n = int(input('input number:'))

print('Divisors of a number', n)

for i in range (1,n//2+1):
    if not n%i:
        print(i, end=' ')
print(n)