n=int(input())
ans=[]
ka=0
kb=0
kc=0
for i in range(n,0,-1):
  if i%3==0:
    ka+=1
  if i%3==1:
    kb+=1
  if i%3==2:
    kc+=1
print(ka,kb,kc)


'''
可通過測資的程式碼
'''

n=int(input())
ka=0
kb=0
kc=0
for i in range(0,n):
  if i%3==0:
    ka+=1
  if i%3==1:
    kb+=1
  if i%3==2:
    kc+=1
print(ka,kb,kc)
