# Divisible by 2 by 3 by 5 and not by 10

x = int(input('Input number:'))

if (x%2 and not x%3 and not x%5 and x%10):
    print("It is Good!")
else:
    print("It is NOT Good")