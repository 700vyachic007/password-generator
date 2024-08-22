from random import*

def password_generator():
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    ambiguous_characters = "il1Lo0O"

    # переменная для хранения всех возможных символов
    chars = ''

    quantity = int(input("Какое количество паролей вы желаете создать? "))
    pas_len = int(input("Введите длину желаемого пароля: "))
    include_digits = input("Включать ли цифры 0123456789? (да / нет) ")
    include_uppercase = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да / нет) ")
    include_lowercase = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да / нет) ")
    include_symbols = input("Включать ли символы !#$%&*+-=?@^_? (да / нет) ")
    exclude_ambiguous = input("Исключать ли неоднозначные символы il1Lo0O? (да / нет) ")

    if include_digits.lower() == 'да':
        chars += digits
    if include_uppercase.lower() == 'да':
        chars += uppercase_letters
    if include_lowercase.lower() == 'да':
        chars += lowercase_letters
    if include_symbols.lower() == 'да':
        chars += punctuation
    if exclude_ambiguous.lower() == 'да':
        chars = ''.join([ch for ch in chars if ch not in ambiguous_characters])

    passwords = []
    for _ in range(quantity):
        password = ''.join(choice(chars) for _ in range(pas_len))
        passwords.append(password)

    return passwords

for pwd in password_generator():
    print(pwd)