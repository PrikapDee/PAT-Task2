#ques 9 write a program that takes a string  and returns the no. of words in it.
sent=input("enter any stenance")
print(sent)
word_count=1
for x in sent:
    if(x==' '):
        word_count=word_count+1

print(word_count)