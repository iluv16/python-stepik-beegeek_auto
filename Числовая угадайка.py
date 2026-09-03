import random

def is_started():   # функцмя для повторения начальных значений
    if input("Хотите задать диапазон угадываемых чисел? ").lower() in ["lf", "да", "конечно", "yes"]:
        n = int(input("До какого числа будем отгадывать? "))
    else:
        n = 100
    a = random.randint(1, n)
    counter = 0
    return n, a, counter


def is_valid(digit):    # функция для проверки правильности введенного пользователем значения
    if digit.isdigit() and 0 < int(digit) < n:
        return True
    else:
        return False


print("Добро пожаловать в числовую угадайку")   # ПОГНАЛИИИИИИИИИ
n, a, counter = is_started()    # присвоила возвратные значения функции переменным кода

while True:
    str = input(f"С тебя число от 1 до {n}: ")
    if is_valid(str):
        dig = int(str)
    else:
        print(f"A может быть все-таки введем целое число от 1 до {n}?")
        continue

    counter += 1

    if dig < a:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    elif dig > a:
        print("Ваше число больше загаданного, попробуйте еще разок")
    else:
        print("Вы угадали, поздравляем!")
        print(f"Ваше количество попыток отгадать число: {counter}")

        desision = input("Вы хотите еще поиграть? ").lower()

        if desision in ["lf", "да", "конечно", "yes"]:
            n, a, counter = is_started()    # вот для этого момента кода я сделала данную функцию:) 
        else:
            break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")