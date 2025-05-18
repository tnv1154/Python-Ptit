
def check(s1, s2):
    if len(s1) != len(s2):
        return False
    mp1 = {}
    mp2 = {}
    for i in s1:
        if i not in mp1:
            mp1[i] = 0
        mp1[i] += 1
    for i in s2:
        if i not in mp2:
            mp2[i] = 0
        mp2[i] += 1
    for k, val in mp1.items():
        if k not in mp2 or val != mp2[k]:
            return False
    return True


def main():
    for i in range(int(input())):
        s1 = input()
        s2 = input()
        if check(s1, s2):
            print(f"Test {i+1}: YES")
        else:
            print(f"Test {i+1}: NO")

if __name__ == "__main__":
    main()