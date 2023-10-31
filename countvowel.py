str=input()
vowel="aeiouAEIOU"
v=0
i=0
while i<len(str):
  if str[i] in vowel:
    v+=1
  i+=1
print("No of vowels in the given string are: ",v)
