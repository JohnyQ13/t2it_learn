# BANK cash value

#Check input division by 10
while True:
    cash = int(input('input cash value:'))
    if not cash % 10:
        cash = int(cash)
        break
    else:
        print('ERROR: Input value division by 10')

lob = [1000, 500, 200, 100, 50, 20, 10] # list of bills

print(f'You want cash {cash}, we have bills {lob}')

result = {}

for id, item in enumerate(lob):
    count = cash // lob[id]
    if count:
        result[lob[id]] = count
        cash %= lob[id]
print('You bills:')

for id, count in result.items():
    print(f'{id} UAH - {count} bills')