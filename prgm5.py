 #ques 5 write program that takes a string and retuns true  if it is pallindrome, false otherwise
str1 ="PCPkPCPK"
len=len(str1)
print(len)
i=0
if(str1[i]!=str1[len-i-1]):
    print("false")
while(i<len/2):
    if(str1[i]==str1[len-i-1]):
        i=i+1
        print("true")

    elif(str1[i]!=str1[len-i-1]):
         i=i+1
         print("false")