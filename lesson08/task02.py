# birth       - 3 heads
# 0 ... 100    - 3 heads (50) : 153
# 101 ... 200 - +2 heads (150): 300 + 100 + 3 = 403
# 201 ...     - +1 heads (300): 300 + 200 + 100 + 3 = 603

age = int(input("Input the age of dragon:"))

total = 3

if age <= 100:
    total += age * 3
elif age <= 200:
    total += 100 * 3 + (age - 100) * 2
elif age > 200:
    total += 100 * 3 + 100 * 2 + (age - 200) * 1
msg = f"Dragon has {total} heads"
print(msg)
