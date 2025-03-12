
"""Tìm số có tần suất lẻ duy nhất trong mảng a
Sử dụng phép toán XOR (^)
a ^ a = 0 => số có tần suất chẵn sẽ bị triệt tiêu
a ^ 0 = a
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in a[1:]:
        ans = ans ^ i
    print(ans)