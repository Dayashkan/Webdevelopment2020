def xor(x,y):
    if((x==0 and y==0) or (x==1 and y==1)):
        return 0
    else:
        return 1

x, y = input().split()
x,y= int(x),int(y)
print(xor(x,y))