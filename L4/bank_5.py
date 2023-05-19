# not done
# BANK cash value min value

#Check input division by 10
while True:
    cash = int(input('input cash value:'))
    if not cash % 10:
        cash = int(cash)
        break
    else:
        print('ERROR: Input value division by 10')

limlob = [10, 20, 50, 100]
lob = [200, 500, 1000] # list of bills
count = int(0)

print(f'You want cash {cash}, we have bills {lob}')

result = {}
if cash <= 1800:
    for id, item in enumerate(limlob):
        count = cash // limlob[id]
        if count and count <= 10 and not (cash % limlob[id]):
            result[limlob[id]] = count
            cash %= limlob[id]
        else:
            cash -= limlob[id+1]
            print('cash:',cash)
            id -= 1
            print('id:',id)
        print(count)
print('You bills:')

for id, count in result.items():
    print(f'{id} UAH - {count} bills') 