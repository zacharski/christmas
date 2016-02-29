
def level1(xp):
    if xp > 70:
        print('C')
    elif xp > 80:
        print('B')
    else:
        print('A')

def level2(xp):
    if xp > 70:
        print('C')
    if xp > 80:
        print('B')
    if xp > 90:
        print('A')

def level3(xp):
    if xp > 90:
         print('A')
    elif xp > 80:
        print('B')
    else:
       print('C')

print("Problem 2:")
print("level1(92):")
level1(92)
print("level2(92):")
level2(92)
print("level3(92):")
level3(92)
