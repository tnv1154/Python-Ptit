"""Cho dãy số A[] có N phần tử là các số nguyên dương.
Với mỗi số nguyên K, hãy tính xem có thể tách dãy số A thành ít nhất bao nhiêu nhóm
sao cho mỗi số trong nhóm đều có thể tìm được ít nhất một số khác cùng nhóm có chênh lệch"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
group = 1
for i in range(1, n):
    if arr[i] - arr[i-1] > k:
        group += 1
print(group)