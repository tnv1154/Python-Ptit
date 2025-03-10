
s = input()
cnt = 0
if len(s) == 1:
    cnt += 1
else:
    while True:
        if len(s) == 1:
            break
        cnt += 1
        sum = 0
        for i in s:
            sum += ord(i) - ord("0")
        s = str(sum)
print(cnt)
