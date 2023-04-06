ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

index = 0
while index < len(ls):
    print(ls[index], end=' ')
    index += 1

print()

index = len(ls) - 1

while index >= 0:
    print(ls[index], end=' ')
    index -= 1
