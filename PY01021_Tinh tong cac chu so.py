
for i in range(int(input())):
    s = input()
    sum = 0
    al = ""
    for j in s:
        if j.isdigit():
            sum += int(j)
        else:
            al += j
    al = sorted(al)
    for j in al:
        print(j, end="")
    print(sum)
