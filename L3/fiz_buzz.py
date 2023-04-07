def is_positive_number(num):
    try:
        num = int(num)
        if num > 0:
            return True
        else:
            return False
    except ValueError:
        return False

while True:
    fizz = int(input('Input fizz:'))
    buzz = int(input('Input buzz:'))
    limit = int(input('input limit:'))

    if is_positive_number(fizz) and is_positive_number(buzz) and is_positive_number(limit):
        fizz = int(fizz)
        buzz = int(buzz)
        limit = int(limit)
        break
    else:
        print('ERROR: Input positive number')

for i in range(1,limit+1):
    if (not i%fizz and not i%buzz):
        print('FB', end=' ')
    elif not i % fizz:
        print('F', end=' ')
    elif not i % buzz:
        print('B', end=' ')
    else:
        print(i, end=' ')