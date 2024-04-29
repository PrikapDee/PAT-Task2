#ques4 no. of unique chars in string
str1=input("Enter one string :")
newstring=str()
str1=str1.lower()


for x in str1:
    if x not in  newstring:
        newstring=newstring + x

print(newstring)
print("no. of unique chars",len(newstring))






