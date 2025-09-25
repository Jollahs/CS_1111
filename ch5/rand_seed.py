import random

print("Without setting a seed:")
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

print("\nWith seed = 42:")
random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

print("\nWith seed = 42 (again):")
random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

print("\nWith seed = 100:")
random.seed(100)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
