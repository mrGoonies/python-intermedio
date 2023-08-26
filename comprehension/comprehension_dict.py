letters: list = ['a', 'b', 'c', 'd', 'e']
numbers: list = [1, 2, 3, 4, 5]

# Creamos un diccionario a partir de dos listas
my_dict: dict = {key: value for key, value in zip(letters, numbers)}
print(my_dict)

my_new_dict: dict = {i: i*2 for i in range(1, 101) if i % 2 == 0}
print(my_new_dict)



