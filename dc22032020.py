a=input().split()
b=input().strip()
for i in range(1,len(a)-1):
	if a[i]==b:
		a[i-1],a[i+1]=a[i+1],a[i-1]
print(*a)