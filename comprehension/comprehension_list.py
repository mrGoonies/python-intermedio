# Creando una lista de forma tradicional

numbers: list = list()

for i in range(10):
    numbers.append(i)

print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creando una lista con comprensión de listas
list_comprehension: list = [i for i in range(10)]
print(list_comprehension)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Aplicando condiciones. Agregamos sólo valores pares.
list_comprehension: list = [i for i in range(1, 101) if i % 2 == 0]
print(list_comprehension)
