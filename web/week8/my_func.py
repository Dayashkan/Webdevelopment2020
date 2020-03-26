def even(x):
    if x%2 == 0:
        return True
    return False

for i in range(1, 10):
    print(i,even(i))