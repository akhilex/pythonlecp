str=input()
vowel="aeiouAEIOU"
v=False
i=0
while i<len(str):
  if str[i] in vowel:
    v=True
    break
  i=i+1
if v:
  print("It contains vowel")
else:
  print("It doesnot conatain vowel")
  
  
