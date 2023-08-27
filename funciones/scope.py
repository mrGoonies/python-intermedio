# Ambito global
name: str = "Juan"
random_value: int = 10


def saludo():
    # Ambito local
    new_name: str = "Pedro"
    print(f"Hola {new_name}. Solo puedo ser accedido dentro de la funcion.")


def increment_value():
    global random_value
    random_value = random_value + 10

    return random_value


print(name)
saludo()

# Generando un error. NameError: name 'new_name' is not defined
# print(new_name)

print(random_value)
# 10
print(increment_value())
# 20
print(random_value)
# 20
