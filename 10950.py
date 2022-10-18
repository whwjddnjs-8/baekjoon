repeat = int(input())
array = []

for i in range(repeat) :
    a = 0;
    b = 0;
    a,b = map(int, input().split())
    array.append(a+b)

for j in array :
    print(j)
