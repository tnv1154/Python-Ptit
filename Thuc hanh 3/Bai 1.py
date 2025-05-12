
def check(se1, se2):
    if len(se1) != len(se2):
        return False
    for i in range(len(se1)):
        if se1[i] != se2[i]:
            return False
    return True

n, m = map(int, input().split())
se1 = set(list(map(int, input().split())))
se2 = set(list(map(int, input().split())))
arr1 = list(se1)
arr2 = list(se2)
if check(arr1, arr2):
    print("YES")
else:
    print("NO")