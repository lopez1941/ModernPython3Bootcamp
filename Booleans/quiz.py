from random import randint
num = randint(1, 1000)

print(f"Your number is: {num}")
if (num % 2):
    print("odd")
else:
    print("even")