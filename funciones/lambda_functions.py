def increment(x: int) -> int:
    return x + 1


# Refactorizando función con lambda
new_increment = lambda x: x + 1

print(increment(5))
# 6
print(new_increment(5))
# 6
