print("Problem 1c A:")
x = [2, 10, 5, 15, 3, 6, 1]
for g in range(len(x)):
    if g > 5:
        print(x[g])

print("Problem 1c B:")
x = [2, 10, 5, 15, 3, 6, 1]
g = 0
while g < len(x):
    if g > 5:
        print(x[g])
    g = g + 1

print("Problem 1c C:")
g = 0
s = 0
while g < 7:
    if g > 4:
        s = s + g
    g = g + 1
print(s)
