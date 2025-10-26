for i in range(5): 
     print(i, end=" ")
for i in range(5):
     print(i, end=" ")
for ii in "qwerty":
     print(ii)
     print(1, end=" ")

n = 10
while n > 0:
    print(1, end=" ")
    n -= 1
    # зменшує значення на 1

while n > 0:
    if n % 2 == 0:
        n -= 1
        continue
    elif n == 3:
        break
    print(n, end="  ")
    n -= 3


# Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач).

n2 = int(input("Enter the number: "))

for i in range(n2):
    print("Hallo, Python!")

# Дано два цілих числа a і b (a ≤ b). Виведіть всі числа від a до b включно.

n3 = int(input("Enter the number1: "))
n4 = int(input("Enter the number2: "))
list_nums = []
while n3 <= n4:
    list_nums.append(n3)
    n3 += 1

# print(list_nums)
print(" ,".join(map(str, list_nums)))

# Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, з якої слід починати відлік.

n5 = int(input("Enter the amount of seconds: "))
print(n5)
while n5 > 0:
    n5 -= 1
    print(n5)
print("Start!")

# Користувач вводить кількість навчальних предметів n, а потім, відповідно, оцінки учня з n навчальних предметів. Визначте середню оцінку.

subj = int(input("Enter the amount of subjects: "))
sum_of_grades = 0
for i in range(0, subj):
    grade = int(input("Enter the grage one by one: "))
    sum_of_grades += grade
    i += 1

average = sum_of_grades / subj
print(f"Your averege is {average:.2f}")

# Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.

n = int(input("Enter what number you want to print: "))
m = int(input("Enter how nany times you want to print it: "))

for i in range(0, m):
    print(n, end=" ")
    i += 1

# Напишіть програму для друку цілих чисел від n до 0 із виведенням біля кожного числа кількості символів #, що дорівнює значенню числа.

n6 = int(input("Enter the number: "))
for n in range(n6, 0, -1):
    print(n6, "#" * n6)
    n6 -= 1

# Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n

n7 = int(input("Enter the number: "))

for n in range(1, n7 + 1):
    print(str(n) * n)
    n += 1

# Намалювати сходинки як у вихідних даних, використовуючи символи пропуску і решітки #, коли на вхід програми подається ціле число n - кількість сходинок.

n8 = int(input("Enter the number: "))
for n in range(1, n8 + 1):
    print("#" * n)

# За даним цілим додатнім числом n обчисліть n! - значення факторіалу цього числа.

n9 = int(input("Enter the number: "))
fact = 1
for i in range(2, n9 + 1):
    fact *= i

print(fact)

# Автогонщик в перший день ралі проїхав d км. Кожен наступний день він збільшував пробіг на 10% від пробігу попереднього дня. Через скільки днів автоспортивних змагань сумарний пробіг автомобіля за всі дні перевищить t км і яке значення сумарного пробігу? Введення даних користувачем відбувається в порядку: d, t.

d = int(input("Enter the first day distance (km): "))
t = int(input("Enter the full needed distance (km): "))
time = 1
final_d = d
while final_d < t:
    d = (d * 1.1)
    final_d += d
    time += 1

print(f"{final_d:.2f} km for {time} days")

# Дано ціле число n. З чисел 1, 4, 9, 16, 25, …​ надрукувати ті, які не перевищують n. (зверніть увагу на задану послідовність)

n10 = int(input("Enter the number: "))
i = 1
j = 2
while i < n10:
    print(i, end=", ")
    i = j ** 2
    j += 1

# Дано цілі числа a і b. Обчислити a ^ b (a в степені b), не використовуючи операцію піднесення до степеня.

a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))

for i in range(2, b):
    a *= a
    i += 1
print(a)

# Дано натуральне число n. Визначити, чи є воно автоморфним числом.

n11 = int(input("Enter the number: "))

squared = str(n11 ** 2)

print(squared[-len(str(n11)):] == str(n11))

# Дано натуральне число n. Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.

n12 = int(input("Enter the number: "))

i = 1
list_of_nums = []

while len(str(i)) <= n12:
    if len(str(i)) == n12 and (i % 2) != 0:
        list_of_nums.append(i)
    i += 1
list_of_nums.sort(reverse=True)
print(", ".join(map(str, list_of_nums)))

# --------------------------
# n2 = (10 ** (n12)) - 1

# while len(str(n2)) == n12:
#     if (n2 % 2) != 0:
#         print(n2, end=", ")
#     n2 -= 1

# Написати програму для обчислення суми цифр цілого числа n. Програма має враховувати, що на вхід може подаватися ціле від’ємне число.

n13 = int(input("Enter the number: "))
n13 = str(n13)
sum = 0
for i in range (0, len(n13)):
    if n13[i].isdigit():
        sum += int(n13[i])

print(sum)

# Напишіть програму для отримання рядка Фібоначчі від 0 до n, де n - ціле число.

n14 = int(input("Enter the number: "))

a = 0
b = 1
while a < n14:
    print(a, end= ", ")
    temp = a
    a = b
    b += temp

# За введеним користувачем цілим числом n визначте n-е число Фібоначчі

n15 = int(input("Enter the number: "))

a = 0
b = 1
i = 1
while i < n15:
    temp = a
    a = b
    b += temp
    i += 1
print(a)
