# Напишіть програму, яка приймає від користувача рядок, і відображає 
# цей рядок у верхньому і нижньому регістрах.

message = input("Enter your message: ")
print(message.lower())
print(message.upper())

# Скласти програму, яка запитує назву баскетбольної команди і повторює 
# її на екрані зі словами: This is a champion!.

team_name = input("Enter the name of the team: ")
print(f"{team_name}: this is a champion!")

# Дано натуральне число. Знайти число, що отримується при прочитанні 
# його цифр справа наліво.

n = input("Enter a natural number: ")
print(n[ : :-1])

# Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша 
# буква кожного слова була великою, а інші літери - малими. 
# (метод s.title())

message2 = input("Enter your message: ") 
print(message2.title())

# Дано рядок. Визначити порядковий номер першої вказаної букви.
#  Якщо такої літери немає, вивести нуль.

string = input("Enter your message: ")
print(string)
string = string.lower()

letter = input("Enter one letter: ").lower()
check = string.find(letter)

# if letter in string:
if check == (-1):
    print("0")
else:
    print(string.index(letter) + 1)


# # Напишіть програму, яка по введеному числу n від 1 до 9 виводить на екран n пінгвінів з відповідним номером - число від 1 до n. Зображення одного пінгвіна має розмір 5 x 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець. Дозволяється вивести порожній стовпець після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна із вихідних даних. Врахуйте, що виведення на екран виконується порядково, а не «попінгвінно».

n2 = int(input("Enter how many pinguins do you want till 9: "))

string1 = "    _~_     " * n2
string2 = "   (o o)    " * n2
string3 = r"  /  V  \   " * n2
string5 = "   ^^ ^^    " * n2
# nums = "1 2 3 4 5 6 7 8 9"[:2*n2]

# string4 = " /(  " + "  )\\   /(  ".join(nums.split()) + "  )\\ "

print(string1)
print(string2)
print(string3)
for n in range(1, n2 + 1 ):
    print(f" /(  {n}  )\\  ", end="" )

# print(string4)
print ("\n" + string5)

# У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.

k = input("Enter your words (255 symbols max):")
k = k.split() 
# print(k)
print(" ".join(k))


# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.
# ex = input("Enter an addition or subtraction expression of any length using only single-digit numbers:\n")

sum = int(ex[0])

for i in range(1, len(ex), 2):
    if ex[i] == '+':
        sum += int(ex[i+1])
    elif ex[i] == '-':
        sum -= int(ex[i+1])
print(sum)

# # інший варіант
# ex_plus = ex.replace("-","+-")
# parts = ex_plus.split("+")
# sum_ex = sum(map(int, parts))
# print(sum_ex)

# ------------------------------
# my_list = ["12", 4, 6]
# for el in range(len(my_list)):
#     my_list[el] = str(my_list[el])
# new_list = list(map(int, my_list))
# print(new_list)
# ------------------------------

# Напишіть програму, на вхід якої даються чотири числа a, b, c і d, кожне у своєму рядку. Програма повинна вивести фрагмент таблиці множення для всіх чисел відрізка [a; b] на всі числа відрізка [c; d]. Числа a, b, c і d є натуральними і не перевищують 10, a ≤ b, c ≤ d. Дотримуйтесь формату виведення як у вихідних даних. Для поділу елементів всередині рядка використовуйте \t - символ табуляції. Зауважте, що лівим стовпчиком і верхнім рядком виводяться самі числа із заданих відрізків

print("Please enter 4 natural numbers, that are less or equal to 10. a ≤ b, c ≤ d")
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

original_list = [a, b, c, d]
list_1 = []
list_2 = []
list_3 = []
list_4 = []

for i in original_list:
    list_1.append(i * a)
for j in original_list:
    list_2.append(j * b)
for k in original_list:
    list_3.append(k * c)
for l in original_list:
    list_4.append(l * d)

original_list.insert(0, " ")
list_1.insert(0, a)
list_2.insert(0, b)
list_3.insert(0, c)
list_4.insert(0, d)


print("\t".join(map(str, original_list)))
print("\t".join(map(str,list_1)))
print("\t".join(map(str,list_2)))
print("\t".join(map(str, list_3)))
print("\t".join(map(str,list_4)))


# Напишіть програму для друку літери A за допомогою введеного користувачем символа.

sym = input("Enter your symbol: ")
print(f"""   {sym}{sym}{sym}
  {sym}   {sym} 
  {sym}   {sym} 
  {sym}{sym}{sym}{sym}{sym} 
  {sym}   {sym} 
  {sym}   {sym} 
  {sym}   {sym} """)

# Напишіть програму, яка визначає, чи є у введеному рядку десяткові цифри, і виводить найбільше число, яке можна скласти з цих цифр. Провідних нулів у числі бути не повинно (за винятком числа 0, запис якого містить рівно одну цифру). Гарантовано, що у рядку є принаймні одна цифра. Вхідний рядок містить довільні символи. Програма повинна вивести найбільше число, яке можна скласти з присутніх в рядку десяткових цифр.
# Вхідні дані:
# Release Date: July 27, 2008
# Last Updated: February 22, 2018
# Вихідні дані:
# 872200
# 822210
mess = input("Enter your date: ")
list_of_nums = []
for i in mess:
    if i.isdigit():
        list_of_nums.append(i)

list_of_nums.sort(reverse=True)
print("".join(list_of_nums))