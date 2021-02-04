x = int(input())
y = int(input())
z = int(input())
n = int(input())

# 0<=i<=x
# i+j+k!=n
list_co=[]
temp=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            sum=i+j+k
            if (sum!=n):
                temp=[i,j,k]
                list_co.append(temp)
print(list_co)