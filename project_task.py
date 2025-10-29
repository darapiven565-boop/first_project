print("=== Помічник користувача ===")
    
def check_password():
    password = input("Введіть пароль: ")
    if len(password) < 8:
        print("=== Пароль має містити більше 8 символів. Введіть новий пароль ===")
        password = input("Введіть пароль: ")
    while not (any(ch.islower() for ch in password) and any(ch.isupper() for ch in password)):
        print("=== Пароль має містити велику і малу літеру. Введіть новий пароль ===")
        password = input("Введіть пароль: ")
    while not (any(ch.isdigit() for ch in password)):
        print("=== Пароль має містити цифру. Введіть новий пароль ===")
        password = input("Введіть пароль: ")
    while any(ch.isspace() for ch in password):
        print("=== Пароль не має містити пробіл. Введіть новий пароль ===")
        password = input("Введіть пароль: ")
    print("Пароль надійний!")