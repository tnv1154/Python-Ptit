
s = input()
ans = ""
cnt = 0
for i in s[::-1]:
    cnt += 1
    ans += i
    if cnt % 3 == 0 and cnt != len(s) :
        ans += ","
print(ans[::-1])