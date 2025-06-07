
n = int(input())
arr =  list(map(int, input().split()))
st = []
for i in range(n):
    if st and (st[-1] + arr[i]) % 2 == 0:
        st.pop()
    else:
        st.append(arr[i])
print(len(st))