#Сума двох чисел: Написати програму, яка зчитує два цілих числа та виводить їх суму.
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
print(n1 + n2)

#Гіпотенуза: За двома катетами прямокутного трикутника знайти довжину його гіпотенузи.
n3 = float(input("Enter cathetus1: "))
n4 = float(input("Enter cathetus2: "))
hypotenuse = (n3 ** 2 + n4 ** 2) ** 0.5
print("Hypotenuse is", hypotenuse)

#Двічі: Написати програму, яка зчитує ціле число та виводить його двічі.
n5 = int(input("Enter number: "))
print(n5, n5)

#Привіт, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить привітання.
name = str(input("Enter your name: "))
print("Good morning, " + name + "!")

#Прощавай, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить прощання.
name2 = str(input("Enter your name: "))
print("Goodbye, " + name2 + "!")

#Вік через рік: Напишіть програму, яка запитує ім'я користувача та його вік. Потім виведіть повідомлення, яке повідомляє, скільки йому буде років через рік.
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

#Площа прямокутника: Напишіть програму, яка запитує довжину та ширину прямокутника, а потім обчислює та виводить його площу.
l = float(input("Enter length: "))
w = float(input("Enter width: "))
a = l * w
print("Area is", a)

#Конвертер валют: Запропонуйте користувачеві ввести суму в одній валюті (наприклад, доларах), а потім виведіть цю суму в іншій валюті (наприклад, євро), використовуючи заздалегідь визначений коефіцієнт обміну.
n6 = float(input("Enter the amount of euros: "))
dollar = 1.17
print("You have ", n6 * dollar, "dollars")

#Вартість покупки: Запитайте користувача назву товару, його ціну та кількість. Обчисліть загальну вартість покупки та виведіть її на екран.
item = input("Enter your item: ")
price = float(input("Enter the price: "))
amount = int(input("Enter amount of products: "))
print("Your total for", amount, item, "is", price * amount)

#Температура: Напишіть програму, яка перетворює температуру з градусів Цельсія на Фаренгейт. Запитайте користувача температуру в градусах Цельсія.
c = int(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("It is", f, "degrees Farenheit")
