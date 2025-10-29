#1

value = "12 14 16 18 20 93 45 78 1 4 5"
list_of_values = value.split()
print(list_of_values[len(list_of_values) // 2:])

# 2

value_2 = "12 14 16 18 20 93 45 78 1 4 5"
list_of_values_2 = value_2.split()
print(list_of_values_2[-2:] + list_of_values_2[:-2])

# 3

lang = "English Spanish French German Italian Portuguese Dutch"
list_of_languages = lang.split()
list_of_languages.sort()
print(list_of_languages)

# Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.

value = "apple banana cherry orange"
value_list = value.split()
print(value_list[::-1])

# Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

value_list = [12, 14, 56, 8, 6, 799, 56, 2, 3]
value = " ".join(map(str,value_list[0::2]))
print(value)