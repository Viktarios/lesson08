#input block
age = int(input("Input the age of dragon:"))


# foole-proof
if age <= 0:
    msg = "User Data was invalid"
else:
    total = 3

    if age <= 100:
        total += age * 3
    elif age <= 200:
        total += 100 * 3 + (age - 100) * 2
    else:
        total += 100 * 3 + 100 * 2 + (age - 200) * 1

        msg = f"Dragon has {total} heads"

print(msg)