# Функція для додавання
def add(x, y):
    return x + y

# Функція для віднімання
def subtract(x, y):
    return x - y

# Функція для множення
def multiply(x, y):
    return x * y

# Функція для ділення
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

# Головна функція програми
def main():
    print("Скористайтеся калькулятором:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Виберіть операцію (1/2/3/4): ")

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == '1':
        print("Результат:", add(num1, num2))
    elif choice == '2':
        print("Результат:", subtract(num1, num2))
    elif choice == '3':
        print("Результат:", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        print("Результат:", result)
    else:
        print("Невірний вибір операції")

if __name__ == "__main__":
    main()