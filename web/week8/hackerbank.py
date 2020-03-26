print("Hello, World!")

n = int(input())
if n%2!=0:
    print("Weird")
elif 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

from __future__ import division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = []
    p = 0
    for i in range ( x + 1 ) :
        for j in range( y + 1):
            for k in range ( z + 1):
                if i+j+k != n:
                    ar.append([])
                    ar[p] = [ i , j, k ]
                    p+=1
    print(ar)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(dict.fromkeys(arr))
    arr.sort()
    print(arr[len(arr)-2])

if __name__ == '__main__':

    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array.append([score, name])

    array.sort()
    min = array[0][0]
    res = [[array[i][0], array[i][1]] for i in range(len(array)) if array[i][0] != min]
    for i in range(len(res)):
        if res[i][0] == res[0][0]:
            print(res[i][1])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for i in range(3):
        sum+=student_marks[query_name][i]
    average = sum/3
    print("%.2f" % average)

