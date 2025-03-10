
def rotate(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('A')
    sum = sum % 26
    ans = ""
    for i in s:
        ans += chr((ord(i) + sum - ord("A")) % 26 + ord("A"))
    return ans

def merge(s1, s2):
    ans = ""
    for i in range(len(s1)):
        xoay = ord(s2[i]) - ord("A")
        ans += chr((ord(s1[i]) + xoay - ord("A")) % 26 + ord("A") )
    return ans

for _ in range(int(input())):
    s = input()
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:]
    s1 = rotate(s1)
    s2 = rotate(s2)
    print(merge(s1, s2))