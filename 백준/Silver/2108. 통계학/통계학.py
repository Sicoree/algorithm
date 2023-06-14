import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr)/len(arr)))#1) 산술평균
print(arr[len(arr)//2])#2) 중앙값


dic=dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])#3) 최빈값
else:
    print(mx_dic[0])#3) 최빈값
    
print(max(arr)-min(arr))#4) 범위