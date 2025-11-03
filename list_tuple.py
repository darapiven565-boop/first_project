# #1

# value = "12 14 16 18 20 93 45 78 1 4 5"
# list_of_values = value.split()
# print(list_of_values[len(list_of_values) // 2:])

# # 2

# value_2 = "12 14 16 18 20 93 45 78 1 4 5"
# list_of_values_2 = value_2.split()
# print(list_of_values_2[-2:] + list_of_values_2[:-2])

# # 3

# lang = "English Spanish French German Italian Portuguese Dutch"
# list_of_languages = lang.split()
# list_of_languages.sort()
# print(list_of_languages)

# # Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.

# value = "apple banana cherry orange"
# value_list = value.split()
# print(value_list[::-1])

# # Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

# value_list = [12, 14, 56, 8, 6, 799, 56, 2, 3]
# value = " ".join(map(str,value_list[0::2]))
# print(value)

# # 6

# string_1 = "New Delhi New York Paris Prague Reykjavik"
# # string_2 = "Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend"
# list_1 = string_1.split()
# list_2 = string_2.split()
# new_list_1 = []

# for word in list_1:
#     if word not in new_list_1:
#         new_list_1.append(word)
# new_list_2 = []

# for word in list_2:
#     if word not in new_list_2:
#         new_list_2.append(word)

# # set_1 = set(list_1)
# # print(len(set_1))
# print(len(new_list_1))
# print(len(new_list_2))

# # Напишіть програму, яка приймає послідовність чисел, розділених комами, від користувача і створює список і кортеж з цими числами.

# value_7 = "7, 9, 12, 4"

# list_7 = value_7.split(", ")
# list_7.append(list_7)
# tuple_7 = tuple(list_7)

# print(list_7)
# print(type(list_7))
# print(tuple_7)
# print(type(tuple_7))

# # Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.

# url = "https://www.namesite.com/folder/index.html"
# url = url.replace("//","/")
# url = url.split("/")
# print(url[1])
# print(url[-1])

# # Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.

# def set_switch(numbers):
#     max_num = numbers.index(max(numbers))
#     min_num = numbers.index(min(numbers))
#     numbers[min_num], numbers[max_num] = numbers[max_num], numbers[min_num]
#     return numbers

# string_9 = "1 13 4 77 45 8 99"
# numbers = list(map(int, string_9.split()))
# print(set_switch(numbers))

# # Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

# def up_lines():
#     list_9 = []
#     while True:
#         line = input("Enter text (empty to leave): ")
#         if line == "":
#             break
#         list_9.append(line.upper())

#     for el in list_9:
#         print(el)

# up_lines()

# # У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.
       
# string = "1 -2 -3 5 6 -3 7 8"
# values = list(map(int, string.split()))
# for i in range(len(values) - 1):
#     if values[i] * values[i + 1] > 0:
#         print(values[i], values[i+1])

# # У рядку через кому перераховані слова. Сформувати з цих слів новий рядок. Слова мають бути відсортовані за спаданням (від Z до A) без урахування регістру і записані через пропуск.

# text = "horse, cat, Parrot, goldfish, dog"
# text_list = text.split(",")
# text_list.sort(key=str.lower, reverse=True)
# print(" ".join(text_list))

# # 12 Напишіть програму для обчислення добутку цілих чисел (без використання циклу for), які вводяться через пропуск користувачем в одному рядку.

# string_12 = "2 5 3"
# list_12 = list(map(int, string_12.split()))

# i = 0
# product = 1
# while i < len(list_12):
#     product *= list_12[i]
#     i += 1
# print(product)

# # 17 Користувач вводить два цілих додатних числа n і m. Напишіть програму, яка створює двовимірний масив розміром n x m і заповнює його символами . і * у шаховому порядку (як у вихідних даних). Лівий верхній кут повинен мати символ ..

# n = int(input("Enter number of row: "))
# m = int(input("Enter number of column: "))

# # for row in range (n):
# #     for column in range(m):
# #         if (row + column) % 2 == 0: #перевірка по координатам кожної точки
# #             print(".", end=" ") 
# #         else:
# #             print("*", end=" ") 
# #     print() #щоб перейти на новий рядок

# result_list = [] #цикл який виведе матрицю
# for row in range (n):
#     loop_list = [] # список в який ми наповнюємо кожний рядок
#     for column in range(m):
#         if (row + column) % 2 == 0: #перевірка по координатам кожної точки
#             loop_list.append(".") 
#         else:
#             loop_list.append("*") 
#     result_list.append(loop_list)

# print(result_list)

# # 13 Напишіть програму для друку елементів певного цілочисельного списку після видалення з нього парних чисел. Значення списку вводяться через пропуск в одному рядку.

# string_13 = "3 44 6 8 9 12 7"
# list_13 = list(map(int, string_13.split()))

# kill_list = []
# for x in list_13:
#     # print(x)
#     if x % 2 == 0:
#         # print(x)
#         kill_list.append(x)
# for y in kill_list:
#     list_13.remove(y)

# print(list_13)

# #  14 Напишіть програму, яка приймає послідовність 4-цифрових двійкових чисел, розділених комами, і друкує числа, які ділиться на 5 без остачі, в рядку і розділені комами.

# string_14 = "0100,0011,1010,1001,1100,0101"
# list_14 = string_14.split(",")
# list_result = []
# for i in list_14:
#     if int(i, 2) % 5 == 0:
#         list_result.append(str(i))

# result = ",".join(list_result)
# print(result)

# # 15 Ви вирішили написати перетворювач коду на Python в код на Java. Так як на Java прийнятий стандарт найменування CamelCase, то ви вирішили навчитися перетворювати імена з underscore в цей формат. Стиль underscore характеризується тим, що слова в імені пишуться маленькими літерами і розділяються між собою символом підкреслення _. Стиль CamelCase означає, що кожне слово пишеться з великої літери і роздільників між словами немає. Отже, вводиться один рядок, що містить ім’я, записане в форматі underscore. Програма виводить рядок, що містить ім’я в форматі CamelCase.

# string_15 = "my_class"
# list_15 = string_15.split("_")
# list_15 = [i.capitalize() for i in list_15]
# result = "".join(list_15)
# print(result)

# # 16. Напишіть програму для видалення кожного третього елемента із цілочисельного списку і друку результуючого списку, доки список не стане порожнім. Початковий список цілих чисел вводиться в одному рядку через пропуск.

# string_16 = "2 5 8 9 4 78 7 1"
# list_16 = list(map(int, string_16.split()))

# # for i in range(0 ,len(list_16)):
# #     if len(list_16) > 2:
# #         print(list_16)
# #         list_16.pop(2)
# #     else:
# #         print(list_16)
# #         list_16.pop(0)
# # print(list_16)
# index = 4
# while list_16:
#     index_2 = index % len(list_16)
#     # print(index)
#     list_16.pop(index_2)
#     print(list_16)


# # 19 Напишіть програму, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5... (число повторюється стільки разів, чому дорівнює). На вхід програми передається невід’ємне ціле число n - стільки елементів послідовності повинна надрукувати програма. На виході очікується

# n = 8
# list_19 = []
# i = 1
# while i > 0:
#     list_19.extend(str(i) * i)
#     i += 1
#     if len(list_19) >= n:
#         break
# # print(list_19)
# k = len(list_19)
# while k > n:
#     list_19.pop(-1)
#     k = len(list_19)

# print(list_19)

# 20. Використовуючи поняття списку, напишіть програму, яка створює 3D масив елементів a x b x c, кожен з яких має значення 0. Значення a, b, c вводяться в одному рядку через пропуск.

string_20 = "3 3 2"
list_20 = list(map(int, string_20.split()))

for i in range(0, list_20[0]):
    list_column = []
    for j in range(0, list_20[1]):
        list_element = []
        for k in range(1, list_20[2]):
            list_element.append("0")
        list_column.append(list_element)
    print(list_column, end=",")
