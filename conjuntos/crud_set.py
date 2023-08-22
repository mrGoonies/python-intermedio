set_country = {'Chile', 'Colombia', 'Perú'}

size_country = len(set_country)
print(size_country)

# Verificar si un elemento se encuentra en el conjunto
print('Chile' in set_country)
print('Argentina' in set_country)

# Agregar elementos al conjunto
set_country.add('Argentina')
print(set_country)

set_country.add('Brasil')
print(set_country)

set_country.update({'Venezuela', 'Uruguay', 'Paraguay', 'Brasil', 'Holanda'})
print(set_country)

# Eliminar elementos del conjunto
set_country.remove('Holanda')
print(set_country)

set_country.discard('Holanda')
print(set_country)

# Limpiar un conjunto
set_country.clear()
print(set_country)

