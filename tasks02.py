# Создать список из трех любых элементов.
var1 = [1, False, "Test Ok"]

# Создать словарь из трех пар ключ-значение.
var2 = {1: "monday", 2: "Tuesday", 0: None}

# Создать множество из трех элементов.
var3 = {True, 0, "Test Fail"}
# Из списка получить элементо с индексом 1

# Напиать условие if с двумя блоками elif и блоком else.
if 2 in var1:
    print("2 in var1")
elif 3 in var1:
    print("3 in var1")
elif 1 in var1:
    print("1 in var1")
else:
    print("1,2,3 not in var1")

# Написать цикл while.
i = len(var1)
while i > 0:
    i -= 1
    print(f"var1[{i}]={var1[i]}")

# Создать список из трех элементов и распечать его элементы с помощью цикла for
var4 = ['one', 2, True]
for i in var4:
    print(i)

# распечатать числа от 0 до 5
for i in range(6):
    print(i, end="; ")
print()

# создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
var5 = "TEST"
if 'E' in var5:
    print('pass')

# Запросить данные у пользователя и распечатать их используя  форматированную строку.
# var6 = input("Enter number 0-9: ")
# print("I {a}like number {b}".format(a="" if var6 == '5' else "don't ", b=var6))

# Распечатать содержимое файла.
print('-'*20)
with open('task1.py', encoding='UTF8') as readfile:
    print(readfile.read())
print('-'*20)


# Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов.
def sum2(a, b):
    if type(a) == int and type(b) == int:
        return a+b
    else:
        print("a or b is not int")
#       return None


print("Test 1 function sum2 = {}".format(sum2(2, 2)))
print("Test 2 function sum2 = {}".format(sum2(2, True)))


# Создать функцию которая принимает любое количество параметров, распечаатать эти параметры.
def print_all_param(*args):
    j = 0
    for s in args:
        print(f"args[{j}]={s}")
        j += 1


print("Test 1 function print all:")
print_all_param()

print("Test 2 function print all:")
print_all_param(2, 3, 8)

print("Test 3 function print all:")
print_all_param(2, True, 'a', None, 'Ups')


print("End")
