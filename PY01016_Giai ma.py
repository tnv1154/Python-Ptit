
for i in range(int(input())):
    s = input()
    kyTu = ""
    for j in range(0, len(s) - 1, 2):
        kyTu = s[j]
        for x in range(int(s[j+1])):
            print(kyTu, end = "")

    print("")