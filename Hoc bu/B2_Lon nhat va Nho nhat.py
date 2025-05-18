
def main():
    while True:
        n = int(input())
        if n == 0:
            return
        arr = []
        for i in range(n):
            arr.append(int(input()))
        arr.sort()
        if arr[0] != arr[-1]:
            print(arr[0], arr[-1])
        else:
            print("BANG NHAU")

if __name__ == "__main__":
    main()