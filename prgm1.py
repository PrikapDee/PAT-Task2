##ques1 count of total no. of vowels
String ="Guvi Geeks Network Private Limited"
#take a variable and intialised its value to 0
count_of_vowles=0

for x in String :
 if(x=='a' or x=='i' or x=='o' or x=='e'or x=='u'):
    count_of_vowles=count_of_vowles +1
#print total count of vowles
print(count_of_vowles)

#ques 1count of each indidiual vowels
#take 5 variables to count the values of vowles
count_of_vowle_A=0
count_of_vowle_E=0
count_of_vowle_I=0
count_of_vowle_O=0
count_of_vowle_U=0
for x in String :
    if x=='a' or x=='A' :
          count_of_vowle_A=count_of_vowle_A+1
          
    elif x=='i' or x=='I' :
          count_of_vowle_I=count_of_vowle_I+1
                
    elif x=='e' or x=='E':
         count_of_vowle_E=count_of_vowle_E +1
    elif x=='u' or x=='U' :
         count_of_vowle_U=count_of_vowle_U+1

    elif x=='o' or x=='O' : 
         count_of_vowle_O=count_of_vowle_O+1
#printing count of each vowels
print("count of A",count_of_vowle_A,"count of I",count_of_vowle_I,"count of O",count_of_vowle_O,"count of U",count_of_vowle_U,"count of E",count_of_vowle_E)