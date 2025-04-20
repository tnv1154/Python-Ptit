import sys

if __name__ == '__main__':
    mp = {}
    i = 0
    inputs = sys.stdin.read().split()
    for _ in range(10):
        s = int(inputs[i])
        s %= 42
        if s not in mp:
            mp[s] = 1
        i += 1
    print(len(mp))