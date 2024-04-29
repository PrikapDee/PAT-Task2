#ques 3 writea program that takes a string and return after removing all the vowels from it
str1=input("Enter one string :")
vowels='aeiou'
newstring=str()
#converting all string into lowercase
str1=str1.lower()
#iteraing string using for loop
for x in str1:
    if x not in vowels:
        newstring=newstring + x
   

print("string without vowels :" + newstring)

## another method
input_from_user=("Enter one string :")
vowles="aeiou"
#use of lambda function 
only_consonants=lambda x:x.lower() not in vowles
#use of filter function to do filteration of consonants from vowels
result="".join(filter(only_consonants,input_from_user))
print(result) 