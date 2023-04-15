# Генерує файл number_list.txt, з нього вичитує значення обробляє задачею fizz-buzz
# виводить на екран та записує до нового файлу result.txt 

import random
# Create random table numbers 3:10
with open('number_list.txt', 'w') as file:
    for _ in range(10):
        numbers = [random.randint(1, 100) for _ in range(3)]
        file.write(' '.join(map(str, numbers)) + '\n')
print("Файл створений та заповнений number_list.txt")

# Відкриваємо файл для читання
with open('number_list.txt', 'r') as file:
    # Читаємо вміст файлу рядками
    lines = file.readlines()
    # Проходимося по кожному рядку
    with open('result.txt', 'w') as new_file:
        for line in lines:
            # Розбиваємо рядок на числа, використовуючи пробіли як роздільник
            numbers = list(map(int, line.split()))
            # Перевіряємо, чи маємо масив з точно 3 чисел
            if len(numbers) == 3:
                for i in range(1,numbers[2]+1):
                    if (not i%numbers[0] and not i%numbers[1]):
                        new_file.write(' '.join(map(str, 'FB ')))
                        print('FB', end=' ')
                    elif not i % numbers[0]:
                        new_file.write(' '.join(map(str, 'F ')))
                        print('F', end=' ')
                    elif not i % numbers[1]:
                        new_file.write(' '.join(map(str, 'B ')))
                        print('B', end=' ')
                    else:
                        new_file.write(''.join(map(str, f'{str(i)} ')))
                        print(i, end=' ')
                print('\n')
                new_file.write(' '.join(map(str, '\n')))
            else:
                print(f"Помилка: рядок містить менше або більше 3 чисел: {line.strip()}")
