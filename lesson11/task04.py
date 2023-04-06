from random import randint

a = int(input("Input a: "))
b = int(input("Input b: "))

# active fool-proof

if a > b:
    a, b = b, a

print(randint(a, b))
print(randint(a, b))
print(randint(a, b))
print(randint(a, b))
print(randint(a, b))
print(randint(a, b))
