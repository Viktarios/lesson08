a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))
d = int(input("Input d:"))

# max min arithmetic_avg geometrical_avg
if a > b and a > c and a > d:
    max = a
elif b > c and b > d:
    max = b
elif c > d:
    max = c
else :
    max = d

msg = f"Max value is {max}"
print(msg)
arithmetic_avg = (a+b+c+d)/4
geometrical_avg= (a*b*c*d)**(1/4)
msg = f"geometric average is{geometrical_avg}" \
      f"arithmetic average is {arithmetic_avg}"
print(msg)
