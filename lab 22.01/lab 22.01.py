#1ое задание
def ex_1():
    """ отображает на экран
форматированный текст"""
    return "\"“Don't let the noise of others' opinions\
drown out your own inner voice.\"\n\t\t\t\t\t\t\t\t\t\t\t\t”Steve Jobs"


print(ex_1())

#2ое задание
def ex_2(a,b):
    """функция, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними"""
    print(f"между числвми {a} и {b}, содержатся следующие нечетные числа")
    for i in range(a,b + 1):
        if i % 2 != 0:
            print(i, end=" ")

ex_2(1,10)

#3е задание
def ex_3(dlina,napravlenie,simvol):
    """функцию, которая отображает
           горизонтальную или вертикальную линию из некоторого символа"""
    if napravlenie == 1:
        for i in range (dlina):
            print(simvol)

    elif napravlenie == 0:
        print(simvol * dlina)

ex_3(13,1,5)

#4ое задание
def ex_4(a,b,c,d):
    """ функция, которая возвращает максимальное из четырёх чисел"""
    print(f"между числвми {a},{b},{c},{d} самое большое число")

    return max(a,b,c,d)


print(ex_4(1,2,7,4))



#5ое задание
def ex_5(a,b):
    """ефункция, которая возвращает сумму чисел
в указанном диапазоне"""
    print(f"сумма чисел в указанном диапазоне между числами {a} и {b} равна")
    sum = 0
    for i in range(a,b):
        sum += i
    return sum


print(ex_5(3,7))

#6ое задание


def ex_6(a,b):
    """функция, которая проверяет является ли число простым"""
    print(f"число {a}")
    if a % 2 != 0:
        return True
    else:
        return False
print(ex_6(12,1))

#7ое задание
def ex_7(number):
    """функция, которая проверяет является
ли шестизначное число «счастливым»"""
    print(f"число {number}-")
    number_str = str(number)
    first_half = number_str[0:3]
    second_half = number_str[3:6]

    sum_first_half = 0
    sum_second_half = 0

    for i in first_half:
        sum_first_half += int(i)

    for i in second_half:
        sum_second_half += int(i)

    if sum_first_half == sum_second_half:
        print("Это счастливое число")

    else:
        print("Это несчастливое число")

ex_7(157265)














