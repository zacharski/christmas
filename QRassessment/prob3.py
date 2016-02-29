
def f1(a, b):
    a = a - b
    return a

def f2(x, y):
    return f1(y, x)

def f3(a, b):
    x = f1(a, b)
    y = f2(a, b)
    return x + y

print("Problem 3:")
print("f1(5, 7)")
print(f1(5, 7))
print("f2(5, 7)")
print(f2(5, 7))
print("f3(5, 7)")
print(f3(5, 7))
