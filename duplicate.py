l=[]
n=int(input('Enter number of elements:'))
for i in range(n):
   value=int(input())
   l.append(value)
print(l)
new_l=[]
for x in l:
  if x not in new_l:
    new_l.append(x)
print(new_l)
