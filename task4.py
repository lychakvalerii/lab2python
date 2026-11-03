def check_brackets_recursive(s: str, idx: int = 0, balance: int = 0) -> bool:
    # Якщо закриваючих дужок у поточний момент стало більше, ніж відкриваючих
    if balance < 0:
        return False

    # Базовий випадок: дійшли до кінця рядка
    if idx == len(s):
        return balance == 0

    # Змінюємо баланс залежно від поточного символу
    if s[idx] == '(':
        balance += 1
    elif s[idx] == ')':
        balance -= 1

    # Рекурсивний виклик для наступного символу
    return check_brackets_recursive(s, idx + 1, balance)


def task4():
    print("\n--- Завдання 4 ---")
    user_str = input("Введіть рядок з дужками для перевірки: ")

    if check_brackets_recursive(user_str):
        print("Дужки розставлені ПРАВИЛЬНО.")
    else:
        print("Дужки розставлені НЕПРАВИЛЬНО.")

task4()