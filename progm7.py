#7 write a program take a string and returns most frequent characters in it.
str1=input("Enter one string :")
#declaring one new string
most_fre_str=str()
str1=str1.lower()

#for loop to iterate string
for x in str1:
    if x in str1 and str1.count(x)>1:
      most_fre_str= most_fre_str +x

print("most frequent char :"+ most_fre_str)