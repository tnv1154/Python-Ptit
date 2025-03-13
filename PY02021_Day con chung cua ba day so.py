from collections import Counter

for _ in range(int(input())):
    exist = False
    n, m, p = list(map(int, input().split()))
    arr1 = Counter(list(map(int, input().split())))
    arr2 = Counter(list(map(int, input().split())))
    arr3 = Counter(list(map(int, input().split())))
    for x in arr1.keys():
        if x in arr2.keys() and x in arr3.keys():
            for i in range(min(arr1[x], min(arr2[x] ,arr3[x]))):
                exist = True
                print(x, end = " ")
    print("" if exist == True else "NO")
