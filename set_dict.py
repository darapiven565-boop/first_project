# Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.
def task_1():
    to_do = {
        "today": ["clean room", "read", "buy groceries"], "tomorrow": ["cook", "do homework", "call mom"]
    }
    # print(to_do) виводить рядок як записаний весь словник
    print("To do list for today")
    for task in to_do["today"]:
        print("-", task)

    print("To do list for tomorrow")
    for task in to_do["tomorrow"]:
        print("-", task)

# Припустимо, що у нас є словник, в якому ключі є ідентифікаторами, а значення – іменами користувачів. Напишіть програму, яка виводить вітальне повідомлення користувачу на основі його ідентифікатора. Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.

def task_2():
    names = {
        0: "Alice",
        1: "Bob",
        2: "Charlie",
        3: "Diana",
        4: "Ethan",
        5: "Fiona",
        6: "George",
        7: "Hannah",
        8: "Isaac",
        9: "Julia"
    }
    user_id = int(input("Your Id: "))

    if user_id in names:
        print(f"Hello, {names[user_id]}")
    else:
        print("Hello to all!")

# Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.

def task_3():
    films = {
        "The Shawshank Redemption": 1994,
        "The Godfather": 1972,
        "The Dark Knight": 2008,
        "Pulp Fiction": 1994,
        "Forrest Gump": 1994
        }

    sorted_films = dict(sorted(films.items()))
    # for name, year in sorted_films.items(): # З ДВОКРАПКОЮ    
    #     print(f"('{name}': {year}")
    for name in sorted_films.items():
        print(f"{name}")

# Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.
def task_4():
    n = int(input("Enter number: "))
    numbers = {}
    # for i in range(1, n+1):
    #     numbers[i] = i **2
    numbers = {i: i ** 2 for i in range(1, n+1)}

    print(numbers)

# Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.

def task_5():
    n = int(input("Enter number: "))
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [i for i in range(7)]

    # week_dict = {weeks[j]: days[j] for j in range(7)}
    week_dict = dict(zip(weeks, days))
    for d, number in week_dict.items():
        if number == n:
            print(d)

# Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.

def task_5():
        # Задаємо рядок
    string = "Lorem ipsum dolor sit amet"

    # Перетворюємо рядок на список символів
    # Тепер кожен символ (включно з пробілами) — окремий елемент списку
    text = list(string)

    # Створюємо словник, де ключ — символ, а значення — кількість його повторів у списку
    # Для кожного символу i в списку text рахуємо, скільки разів він зустрічається
    letters = {i: text.count(i) for i in text}

    # Виводимо словник на екран
    print(letters)

# Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

def task_7():
    string = "Project Gutenberg offers over 59,000 free eBooks"

    number_count = 0
    alpha_count = 0
    for ch in string:
        if ch.isdigit():
            number_count += 1
        elif ch.isalpha():
            alpha_count += 1
        
    # print(f"LETTER : {alpha_count}")
    # print(f"DIGITS : {number_count}")

    result = {
        "LETTER": alpha_count,
        "DIGITS": number_count
    }

    for key, value in result.items():
        print(key, value)

# Напишіть програму для видалення дублікатів зі списку цілих чисел

def task_8():
    numbers = [1, 2, 4, 88, 5, 9, 5, 65, 88, 88]
    numbers = list(set(numbers))
    print(numbers)

# Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.

def task_9():
    list_of_dict = [
        {"name" : "Alice", "points" : [80, 70, 65, 60]},
        {"name" : "Bob", "points" : [74, 64, 99, 62]},
        {"name" : "Charlie", "points" : [64, 70, 62, 77]},
        {"name" : "Diana", "points" : [92, 74, 87, 61]}
        ]
    for i in list_of_dict:
        print(f"{i["name"]} {min(i["points"])}")
    


    #  # numbers_3 = set(numbers_1).union(set(numbers_2))
    # numbers_3 = set(numbers_1) | (set(numbers_2))
    # # Створимо множини з двох списків (numbers_1 та numbers_2)
    # # difference() - повертає елементи, які є в першій множині, але **немає у другій**
    # print(set(numbers_1).difference(set(numbers_2)))

    # # symmetric_difference() - повертає елементи, які є **тільки в одній з множин**, тобто унікальні для кожної
    # print(set(numbers_1).symmetric_difference(set(numbers_2)))

    # # intersection_update() - змінює першу множину, залишаючи тільки ті елементи, 
    # # які **є у обох множинах** (перетин)
    # (set(numbers_1).intersection_update(set(numbers_2)))
    # print(numbers_1)

# Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.

def task_10():
    numbers_1 = [2, 4, 5, 7, 88]
    numbers_2 = [3, 4, 5, 7, 13, 88]
    
    digit_1 = []
    digit_2 = []

    for num in numbers_1:
        for digit in str(num):  # перетворюємо число у рядок і перебираємо символи
            if digit.isdigit():
                digit_1.append(int(digit))
    print(digit_1)
    for num in numbers_2:
        for digit in str(num):
            if digit.isdigit():
                digit_2.append(int(digit))
    print(digit_2)
    numbers_3 = set(digit_1).symmetric_difference(set(digit_2))

    print(numbers_3)
    print(len(numbers_3))
# task_10()

# Дано три словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. Ключі у всіх словниках – різні, їх є по 3 в кожному словнику. Об’єднайте всі три словники в один і виведіть його вміст. Підказка. скористайтеся оператором **, що використовується для об’єднання довільної кількості словників.

def task_11():
    dict_1 = {
        "a": 42,
        "b": 17,
        "c": 89
    }

    dict_2 = {
        "d": 23,
        "e": 56,
        "f": 91
    }

    dict_3 = {
        "g": 34,
        "h": 78,
        "i": 12
    }

    print({**dict_1, **dict_2, **dict_3})

# Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.

    # функція get_value приймає кортеж (item), який складається з (ключ, значення),
    # і повертає тільки значення (тобто ціну), щоб за нею можна було сортувати
def get_value(item):
    return item[1]

def task_12():

    stocks = {"IBM": 205.55,
    "FB": 10.75, 
    "AAPL": 612.78,
    "ACME": 45.23,
    "HPQ": 37.2,
    }

    # sorted(stocks.items(), key=get_value)
    # перетворює словник у список кортежів і сортує його за значенням (ціною)
    # приклад елемента: ('IBM', 205.55)

    # проходимося по відсортованому списку і виводимо ціни разом із назвами компаній
    for key, value in sorted(stocks.items(), key=get_value):
        print(value, key)

# В рядку записаний текст. Словом вважається послідовність непробільних символів, які йдуть підряд, слова розділені одним або більшим числом пропуском або символами кінця рядка. Для кожного слова з цього тексту підрахуйте, скільки разів воно зустрічалося в цьому тексті раніше.

def task_13():
    text = "var list set tuple list tuple tuple dict var".split()
    result = {}
    for i in text:
        print(result.get(i, 0), end=", ")
        result[i] = result.get(i, 0) + 1

# Напишіть програму, яка зможе підрахувати слова у введеному рядку, розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити число його повторень (без урахування регістру), слова не повинні повторюватися, порядок слів довільний.

def task_14():
    text = "a bb acD bb abc ac BCD a".lower().split()
    result = {}
    # проходимо по кожному слову у списку
    for word in text:
        # метод get() повертає поточне значення ключа word у словнику
        # якщо слова ще немає у словнику, повертає 0
        # потім додаємо 1, щоб збільшити лічильник появ слова
        result[word] = result.get(word, 0) + 1

    for key, value in result.items():
        print(key, value)

# Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.

def task_15():
    list_1 = [2, 5, 8, 11, 10, 9]
    list_2 = [11, 3, 7, 6, 8, 5]

    inters = sorted(list(set(list_1).intersection(list_2)))
    for i in inters:
        print(i, end=" ")
