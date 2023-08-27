# Asignamos valores por defecto a los parámetros de una funcion.
def find_volumen(lenght: int = 1, width: int = 1, depth: int = 1) -> int:
    return lenght * width * depth


def multiply_return_values(x: int, y: int) -> tuple:
    return x * y, x / y


if __name__ == "__main__":
    print(find_volumen(2, 3, 4))
    # 24
    print(find_volumen())
    # 1

    restul_function = multiply_return_values(10, 2)
    print(restul_function)
    # (20, 5.0)
