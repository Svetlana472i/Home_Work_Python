#    Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
#    проверяет, является ли этот день выходным.

# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
num = [1,2,3,4,5]
n = int(input('Введите номер дня недели '))
if n==6 or n==7:
    print('День недели с номером', n, '- это выходной день')
else:
    if n in num:
        print('День недели с номером', n, '- не является выходным днем')
    else:
        print('Число', n, 'не является номером дня недели')