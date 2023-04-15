import sys

# Отримуємо ім'я поточного файлу
filename = sys.argv[0]

# Відкриваємо файл для читання
with open(filename, 'r') as f:
    # Зчитуємо вміст файлу
    code = f.read()

# Відкриваємо новий файл для запису
with open('my_program.py', 'w') as new_file:
    # Записуємо вміст поточного файлу у новий файл
    new_file.write(code)

print("Код був успішно записаний у файл my_program.py")