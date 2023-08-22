set_countries = {'Chile', 'Colombia', 'Perú'}

print(set_countries)
print(type(set_countries))

# Agregando un valor duplicado en el conjunto:
set_countries.add('Chile')
print(set_countries)
# {'Colombia', 'Perú', 'Chile'}

set_types = {'Hello', True, 2, 1.1}
print(set_types)

# Creaando un conjunto desde un string:
set_from_string = set('Hello')
print(set_from_string)
# {'l', 'e', 'H', 'o'}

# Creando un conjunto a partir de una tupla
set_from_tupla = set((1, 2, 3, 4, 5))
print(set_from_tupla)

# Creando un conjunto a partir de un dict (Sólo se agregan los *values*)
set_from_dict = set({'name': 'Juan', 'age': 23})
print(set_from_dict)

# Creando un conjunto a partir de una lista
set_from_list = set(['Gabo', 24])
print(set_from_list)

# Transformando un conjunto a una lista.
# Se pierde el orden de los elementos pero no habrán duplicados
random_numbers = [1, 8, 5, 10, 22, 8, 1]
set_from_random_numbers = set(random_numbers)
unique_random_numbers = list(set_from_random_numbers)

print(unique_random_numbers)
