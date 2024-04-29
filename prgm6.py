#ques 6 longest common substring
#taking 2 string from user
str1=input("Enter one string :")
str2=input("Enter one string :")
#taking one blank string
newstring=str()
#converting string to lower case
str1=str1.lower() 
str2=str2.lower()

for x in str1:
    if x in str2:
        newstring=newstring + x
    
    else :
        newstring= newstring + " "
   

longest_Substring=newstring.split()

print("longest common substrin:"+ max(longest_Substring))