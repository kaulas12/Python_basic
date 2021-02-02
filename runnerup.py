n = int(input())
arr =list(map(int,input().strip().split()))[:n]
a=max(arr)
arr.sort()
for i in arr:
    if(i==a):
        break
    else:
        sum=i
print(sum)   
