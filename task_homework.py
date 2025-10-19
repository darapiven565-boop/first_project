# Задача 1. Середнє трьох чисел
# Користувач вводить три числа. Обчисли середнє арифметичне.
n1 = float(input("Enter number1: "))
n2 = float(input("Enter number2: "))
n3 = float(input("Enter number3: "))
print("Arithmetic mean is", (n1 + n2+ n3) / 3)

# Задача 2. Остача від ділення
# Користувач вводить два числа. Знайди остачу від ділення першого на друге.
n4 = float(input("Enter number1: "))
n5 = float(input("Enter number2: "))
print("The reminder of devision is", n4 % n5)

# Задача 3. Подвоєне число
# Користувач вводить число. Виведи подвоєне значення цього числа.
n6 = float(input("Enter number: "))
print("Double number is", n6 + n6 )

# Задача 4. Конвертація хвилин у секунди
# Користувач вводить кількість хвилин. Обчисли, скільки це буде секунд.
second = 60
minute = int(input("Enter amount of tine in minutes: "))
print("you have spend", minute*second, "seconds")

# Задача 5. Кількість яблук на кожного
# Є n яблук і k учнів. Скільки яблук отримає кожен учень, якщо ділити порівну, і скільки залишиться?
n7 = int(input("Enter the amount of apples: "))
k = int(input("Enter the amount of students: "))
print("Every student gets", n7 // k, "apples")

# Задача 6. Остання цифра числа
# Користувач вводить число. Виведи його останню цифру.

# Задача 7*. Обмін змінних
# Користувач вводить два числа. Після цього потрібно “поміняти” їх місцями і вивести результат.