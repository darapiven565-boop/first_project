# Ви придбали товар на певну суму s. Скільки купюр різного номіналу 
# треба віддати продавцю, якщо починати платити з найбільших? 
# У вас є 1, 2, 5, 10, 100, 500 гривень.

sum = int(input("Enter yor sum: "))
money_500 = sum // 500
sum = sum % 500

money_100 = sum // 100
sum = sum % 100

money_10 = sum // 10
sum = sum % 10

money_5 = sum // 5
sum = sum % 5

money_2 = sum // 2
sum = sum % 2

money_1 = sum // 1
sum = sum % 1

print("You need: 500 -", money_500)
print("100 -", money_100)
print("10 -", money_10)
print("5 -", money_5)
print("2 -", money_2)
print("1 -", money_1)

# 1. Напишіть програму, в якій користувач вводить пароль і якщо він 
# співпадає із наперед визначеним паролем для цього користувача, 
# то виводиться повідомлення Password accepted.. 
# У іншому випадку повідомлення буде Sorry, that is the wrong password..
password = input("Enter your password: ")
password_accept = "Qwerty"

if password == password_accept:
    print("Password accepted!")

else:
    print("Sorry, that is the wrong password.")

# 2. Користувачем вводиться два імені. Використовуючи конструкцію 
# розгалуження програма повинна вивести імена в алфавітному порядку.

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")

if name1 <= name2:
    print(name1, name2)
else:
    print(name2, name1)

# 3. Напишіть програму, яка виводить назви введених чисел. Користувач 
# вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться 
# повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших 
# випадках виводиться слово Unknown.

n = int(input("Enter number: "))

number_of_print = ""

if n == 1:
    number_of_print = "One"
elif n == 2:
    number_of_print = "Two"
elif n == 3:
    number_of_print = "Three"
else:
    number_of_print = "Unknown"

print(number_of_print)

# 4. Користувач вводить дві різних англійські літери в окремих рядках. 
# Напишіть програму, яка виводить повідомлення про місце розташування 
# однієї літери відносно іншої у алфавіті.

letter1 = input("Enter letter1: ").lower
letter2 = input("Enter letter2: ").lower

if letter1 <= letter2:
    print("Letter", letter1, "is first, and letter", letter2, "is second")
else:
    print("Letter", letter2, "is first, and letter", letter1, "is second")

# 5. Напишіть програму, в якій користувач вводить значення температури, 
# і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно 
# вивести повідомлення A cold, isn’t it?. Якщо ж температура становить 
# більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших 
# випадках Nice weather we’re having..
t = int(input("Enter the temperature in celcius: "))
answer = ""

if t <= 0:
    answer = "A cold, isn’t it?"
elif t > 0 and t < 10:
    answer = "Cool."
elif t >= 10:
    answer = "Nice weather we’re having."

print(answer)

# Середній рівень

# Визначте назву геометричної фігури за введеною кількістю її сторін. 
# Програма повинна підтримувати фігури від 3 до 6 сторін. 
# Якщо введена кількість сторін поза межами цього діапазону, 
# програма повинна відображати відповідне повідомлення.
sides = int(input("Enter amount of sides: "))
figure = ""

if sides == 3:
    figure = "triangle"
elif sides == 4:
    figure = "quadrilateral"
elif sides == 5:
    figure = "pentagon"
elif sides == 6:
    figure = "hexagon"
else:
    figure = "unknown! Please, enter number from 3 to 6."

print("Your figure is", figure)

# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, 
# червоний або зелений кольори. Номер 0 має зелений колір, 
# для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. 
# Непарні номери від 11 до 18 - чорні, а парні номери - червоні. 
# Непарні номери від 19 до 28 - червоні, а парні номери - чорні. 
# Непарні номери від 29 до 36 - чорні, а парні номери - червоні. 
# Напишіть програму, яка отримує номер (число від 0 до 36) та показує, 
# чи є номер зеленим, червоним або чорним. Програма повинна враховувати 
# варіант, якщо користувач вводить номер, який знаходиться за межами 
# діапазону від 0 до 36.

n = int(input("Enter the number from 0 to 36: "))

if n == 0:
    print("green")
elif 0 < n <= 10:
    if n % 2 == 0:
        print("black")
    else:
        print("red")
elif 11 <= n <= 18:
    if n % 2 == 0:
        print("red")
    else:
        print("black")
elif 19 <= n <= 28:
    if n % 2 == 0:
        print("black")
    else:
        print("red")
elif 29 <= n <= 36:
    if n % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("Unknown! Please enter number from 0 to 36")

# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

print("Coordinates of A")
x1 = int(input("Enter x-coordinate of A: "))
y1 = int(input("Enter y-coordinate of A: "))
print("Coordinates of B")
x2 = int(input("Enter x-coordinate of A: "))
y2 = int(input("Enter y-coordinate of A: "))

a_length = (x1 ** 2 + y1 ** 2) ** 0.5
b_length = (x2 ** 2 + y2 ** 2) ** 0.5

if a_length < b_length:
    print("Point B is farther from the origin")
elif a_length > b_length:
    print("Point A is farther from the origin")
elif a_length == b_length:
    print("The distance to points A and B is the same.")

# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.


print("Enter coordinates of the point A")
x3 = int(input("Enter the x-coordinates: "))
y3 = int(input("Enter the y-coordinates: "))

print("Enter radius")
r = int(input("Enter radius: "))

if x3 ** 2 + y3 ** 2 == r ** 2:
    print("the point A lies on the circle.")
elif x3 ** 2 + y3 ** 2 < r ** 2:
    print("the point A is inside the circle.")
elif x3 ** 2 + y3 ** 2 > r ** 2:
    print("the point A is outside the circle.")

# Дано натуральное число. Визначити, чи закінчується число парною цифрою.
# Вхідні дані:
# 1234
# 35
# Вихідні дані:
# True
# False
 
 

# Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.
# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
# -3
# 2
# 4
# 2
# Вихідні дані:
# No roots.
# 0.27 and -3.05
# -1.00
# Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне.
# Вхідні дані:
# 2
# 5
# 11
# Вихідні дані:
# True
# False
# False
# Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.
# Вхідні дані:
# 1998
# 3
# 2018
# 2
# Вихідні дані:
# 19
# Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.
# Вхідні дані:
# 2358
# 2227
# 1353
# Вихідні дані:
# *35*
# ***7
# 1353