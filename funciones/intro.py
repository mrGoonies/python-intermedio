# Creando funciones
def show_name(name: str) -> None:
    """
    show_name imprime un nombre en pantalla.

    Args:
        name (str): Nombre que se va a mostrar en pantalla.
    """
    print(name)

def user_age(year_birthday: int) -> int:
    """
    user_age calcula la edad de una persona.

    Args:
        year_birthday (int): Año de nacimiento de la persona.

    Returns:
        int: Edad de la persona.
    """

    return int(2023 - year_birthday)


if __name__ == '__main__':
    show_name('Juan')
    user_age: int = user_age(1990)

    print(f'Tu edad es: {user_age}')


