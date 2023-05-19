

while True:
    num = int(input("Enter positive ODD number:"))
    if num % 2 and num:
        num = int(num)
        break
    else:
        print("Please enter positive ODD number")

def diamond():
    for i in range(1, num+1, 2):
        print((num-i) // 2 * ' ', i*'*', sep='')
    for i in range(num-2, 0, -2):
        print((num-i) // 2 * ' ', i*'*', sep='')

diamond()

