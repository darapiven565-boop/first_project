#1

def name_function (name):
    return (f"Hello, {name}!")

name_input = input("Напишіть ваше ім'я:")
print(name_function(name_input))
#2
def copy_str (string, n):
    return string * n

string = input("Enter your message: ")
number = int(input("Enter the number: "))

print(copy_str(string, number), end= " ")

#3
def sum_a_b(a, b):
    return a + b

num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
print(sum_a_b(num_1, num_2))

# 4
def n_letter (word, n):
    if len(word) < n:
        return word
    return word[:n]

word = input("Enter your message: ")
n = int(input("Enter the number: "))

print(n_letter(word, n))

# 5
def maximum(a, b, c):
    return max(a, b, c)
a = 4
b = 6
c = 3

print(maximum(a, b, c))

# 6

def add_tag (string):
    temp_list = string.split()
    return f"<{temp_list[0]}>{" ".join(temp_list[1:])}</{temp_list[0]}>"

string = input("Enter your tag and string: ")

print(add_tag(string))

# 7 Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.

def season(month):
    if month <=2 or month == 12:
        return "Winter"
    if 3 <= month <= 5:
        return "Spring"
    if 6 <= month <= 8:
        return "Sommer"
    if 9 <= month <= 11:
        return "Autumn"

month = int(input("Enter the number of your month: "))
print(season(month))

# 8  Напишіть функцію для створення гістограми (наприклад, у вигляді *) із заданого списку цілих чисел як у вихідних даних. Формат введення списку чисел як у вхідних даних

def gystogram(numbers):
    numbers = numbers.split(",")
    for i in range(0, len(numbers)):
        numbers[i] = "*" * int(numbers[i])
    numbers = "\n".join(numbers)
    return numbers

n = input("Enter the list of numbers devided by , without spaces: ")

print(gystogram(n))

# Напишіть функцію для визначення, чи рік високосний чи ні.

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return "not a leap year"
        else:
            return "leap year"
    return "not a leap year"

year_1 = 1904
year_2 = 2000
year_3 = 2007
print(leap_year(year_1))
print(leap_year(year_2))
print(leap_year(year_3))

# Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

def rainfall_stats(value):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    rain_month = list(map(float, value.split()))
    overall_rain = sum(map(float, rain_month))
    everage = overall_rain / 12

    min_value = min(rain_month)
    min_month = months[rain_month.index(min(rain_month))]
    
    max_value = max(rain_month)
    max_month = months[rain_month.index(max(rain_month))]

    return (overall_rain, everage, (max_value, max_month), (min_value, min_month) )

data = "22 22 24 49 72 98 101 82 51 40 36 24"

print(rainfall_stats(data))

# На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.
def income_class(price, amount):
    return price * amount

def income(class_A, class_B, class_C):
        
    all_incomes_d = {}
    all_incomes_d['A'] = income_class(class_A[1], class_A[2])
    all_incomes_d['B'] = income_class(class_B[1], class_B[2])
    all_incomes_d['C'] = income_class(class_C[1], class_C[2])
    
    all_income = all_incomes_d['A'] + all_incomes_d['B'] + all_incomes_d['C']

    return ((all_incomes_d), all_income)

category_1 = "A"
price_1 = 20.50
amount_1 = 45
# list_a = [category_1, price_1, amount_1]
price_2 = 15.75
category_2 = "B"
amount_2 = 30 
list_b = [category_2, price_2, amount_2]
category_3 = "C"
price_3 = 10.55
amount_3 = 15
list_c = [category_3, price_3, amount_3]

print(income(list_a, list_b, list_c))



# Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні. Регістр літер, пропуски і знаки пунктуації не враховувати.

def palindrome_check(string):
    string = string.lower()
    string = string.replace(",", "")
    string = string.replace(" ", "")
    string = string.replace(".", "")
    if string == string[::-1]:
        return "that`s a palindrome!"
    return "that`s not a palindrome!"

# треба писати без точки
string_1 = "I am, you are"
string_2 = "No lemon, no melon."

print(palindrome_check(string_1))
print(palindrome_check(string_2))

# Напишіть рекурсивну функцію, яка обчислює суму цілих чисел a і b. З арифметичних операцій використовується тільки додавання одиниці і віднімання одиниці.

def add_number(a, b):
    if b == 0:
        return a
    elif b > 0:
        return add_number(a + 1, b - 1)
    else:  # b< 0
        return add_number(a - 1, b + 1)
# print(add_number(3, -9))

# Дано послідовність цілих чисел, що закінчується числом 0. Напишіть рекурсивну функцію, яка друкує цю послідовність в зворотному порядку. При розв’язуванні цього завдання не можна користуватися списками.
def reverse_order(numbers, index=0):
    if numbers[index] == 0:
        print(numbers[index], end=" ")
        return
    reverse_order(numbers, index + 1)
    print(numbers[index], end=" ")


numbers = list(map(int, "2 15 77 3 0".split()))
reverse_order(numbers)