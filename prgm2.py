#Create a pyramind of numbers from 1 to 20 using for loop
#take a variable of row 
rows = 20
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j,end='')
    print('')
