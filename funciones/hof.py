def increment(x: int) -> int:
    return x + 1


def high_order_function(func, x: int):
    return x + func(x)


print(high_order_function(increment, 2))
# 5


# ejemplo
def apply_operation(operation, x, y):
    return operation(x, y)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


result1 = apply_operation(add, 5, 3)
result2 = apply_operation(subtract, 10, 4)
print(result1)  # Output: 8
print(result2)  # Output: 6
