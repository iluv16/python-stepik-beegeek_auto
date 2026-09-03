import random


def generate_password(length, chars):  # функция для генерации одного пароля
    return random.sample(chars, length)


positive = ["да", "lf", "конечно", "rjytxyj", "yes"]    # списки
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "#$%&*+-=?@^_"
chars = ""

n = int(input("Сколько паролей сгенерировать? "))
l = int(input("Сколько символов долджно быть в пароле? "))
if input("Включать ли цифры 0123456789? ").lower() in positive:
    chars += digits
if input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ").lower() in positive:
    chars += uppercase_letters
if input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ").lower() in positive:
    chars += lowercase_letters
if input("Включать ли символы !#$%&*+-=?@^_? ").lower() in positive:
    chars += punctuation
if input("Исключать ли неоднозначные символы il1Lo0O? ").lower() in positive:
    all_chars = ""
    for i in range(len(chars)):  # исключаем неоднозначные символы
        if chars[i] not in "il1Lo0O":
            all_chars += chars[i]
    chars, all_chars = all_chars, ""
if input("Хочешь исключить какие-нибудь символы? ") in positive:
    your_chars = input("Напиши их: ")
    for i in range(len(chars)):  # исключаем символы, которые вам не нравятся:))))
        if chars[i] not in your_chars:
            all_chars += chars[i]

for i in range(n):  # цикл с генерацией паролей
    print(*generate_password(l, all_chars), sep="")
