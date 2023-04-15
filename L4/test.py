i = 10
while True:
    i -= 1
    if not i: 
        print('One if:',i)
        continue
    if i%2:
        print(i)
    if i < -10: break
print(1%5)

мій_список = "Hello"
# [5, 6, 7, 8]

for i, elem in enumerate(мій_список):
	print(i, elem)
    