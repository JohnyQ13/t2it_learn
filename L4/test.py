# Купюри, доступні в банкоматі
available_notes = {10: 10, 20: 10, 50: 10, 100: 10, 200: 10, 500: 10, 1000: 10}

def withdrawal(amount):
    remaining_amount = amount
    notes_to_withdraw = {}

    # Перевірка наявності достатньої кількості купюр різних номіналів
    for note in sorted(available_notes.keys(), reverse=True):
        while remaining_amount >= note and available_notes[note] > 0:
            notes_to_withdraw[note] = notes_to_withdraw.get(note, 0) + 1
            remaining_amount -= note
            available_notes[note] -= 1

    # Видача готівки, якщо вона можлива
    if remaining_amount == 0:
        print(f"Видача готівки: {amount} грн")
        for note, count in notes_to_withdraw.items():
            print(f"{note} грн: {count} купюр")
    else:
        print("Недостатньо коштів у банкоматі для видачі вказаної суми.")

# Основний код програми
while True:
    amount = int(input("Введіть суму для видачі (або 0 для виходу): "))
    if amount == 0:
        print("Дякуємо, що скористалися нашим банкоматом!")
        break
    elif amount < 0:
        print("Введена некоректна сума.")
        continue
    withdrawal(amount)
