
def main():
    for i in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        a_sort = sorted(a)
        max_val = a_sort[-1]
        max_first_idx = a.index(max_val)
        a.insert(max_first_idx, m)
        am , duong = [], []
        for x in a:
            if x < 0:
                am.append(x)
            else:
                duong.append(x)
        for x in am:
            print(x, end = " ")
        for x in duong:
            print(x, end = " ")
        print()


if __name__ == '__main__':
    main()