fizz = int(input('Input fizz:'))
buzz = int(input('Input buzz:'))
limit = int(input('input limit:'))

for i in range(1,limit):
    if (not i%fizz and not i%buzz):
        print('FB', end=' ')
    elif not i % fizz:
        print('F', end=' ')
    elif not i % buzz:
        print('B', end=' ')
    else:
        print(i, end=' ')