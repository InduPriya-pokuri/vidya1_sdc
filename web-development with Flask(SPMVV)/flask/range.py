'''n = int(input("enter n vAalue:"))
for i in range(1,n+1):
    print(i,end = ' ')'''


'''s = input()
for i in s:
    print(ord(i))'''

n = input().split()
s1 = n[0][0]
s2 = n[1:]
print(s1,'.',sep='',end=' ')
for i in s2:
    print(i,sep='',end=' ')





