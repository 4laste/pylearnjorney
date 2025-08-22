# Инструкция: В каждом задании нужно:
#  1 Объявить функцию точно с тем именем и теми именами параметров, которые указаны в задании.
#  2 Вызвать эту функцию в уже заданном примере, используя переменные или значения, указанные в «Пример вызова». Твой вызов должен точно соответствовать примеру.
#  3 Убедиться, что пример работает.
from wsgiref.util import request_uri


def calculate_area(width, height): # Функция возвращает площадь треугольника
    return width * height
a = 5
b = 10
result = calculate_area(a, b)
print(result)

def greet_user(first_name, last_name): # Функция возвращает строку вида "Привет, [first_name][last_name]!"
    return "Привет, " + first_name + " " + last_name + "!"
name = "Павел"
surname = "Насонов"
message = greet_user(name, surname)
print(message)

def combine_strings(part1, part2, part3): #Функция возвращает строку (комбинированную)
    return part1 + part2 + part3
start = "Начало"
middle = "Середина"
end = "Конец"
final_text = combine_strings(start, middle, end)
print(final_text)

def is_positive(number): #Функция определяет положительное или отрицательное число ей передано
    return number >= 0
print(is_positive(10))
print(is_positive(-5))

def subtract(a, b):
    return a - b
x = 50
y = 15
result = subtract(y, x)
print(result)

def power(base, exponent):
    return base ** exponent
my_base = 2
result = power(my_base, 3)
print(result)

def append_to_list(old_list, new_item):
    return old_list + [new_item]
initial_list = [1, 2, 3]
value_to_add= 4
new_list = append_to_list(initial_list, value_to_add)
print("Исходный список:", initial_list)
print("Новый список:", new_list)
