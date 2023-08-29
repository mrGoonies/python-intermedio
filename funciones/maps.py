numbers = [1, 2, 3, 4, 5]
numbers_v2 = list()

# Forma tradicional de transformar una lista
for i in numbers:
    numbers_v2.append(i**2)

print(numbers)
print(numbers_v2)

# Forma con map
numbers_v3 = list(map(lambda x: x**2, numbers))
print(numbers_v3)

number_v4 = list(map(lambda x: x % 2 == 0, numbers))
print(number_v4)

# Transformando dos listas
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
result_v2 = list(map(lambda x, y: x**y, numbers_1, numbers_2))

print(result)
print(result_v2)


def make_eve(num: int) -> int:
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [100, 241, 92123, 127756, 982, 98]
#           function, iterable
y = list(map(make_eve, x))
print(y)

# Aplicando map en diccionarios
