num = int(input("Enter a series of number : "))
even = 0
odd = 0

for i in range ( 1,num+1) :
    if (i % 2 == 0) :
        even += 1


    else :
        odd += 1

print( "Total Even Numbers :" ,even)
print( "Total odd Numbers :" ,odd)