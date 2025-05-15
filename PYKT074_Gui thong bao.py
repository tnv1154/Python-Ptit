
def main():
    for i in range(int(input())):
        s = input().strip()
        if len(s) < 100:
            print(s)
        else:
            k = 98
            while k >= 0 and s[k].isalpha():
                k -= 1
            print(s[:k])

if __name__ == '__main__':
    main()