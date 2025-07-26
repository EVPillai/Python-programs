str=input('enter a string:')
up=low=ele=0
for x in str:
   if x.isupper():
     up=up+1
   elif x.islower():
     low+=1
   else:
     ele+=1
print('No.of Uppercase characters:',up)
print('No.of Lowercase characters:',low)
print('other special symbols',ele)
