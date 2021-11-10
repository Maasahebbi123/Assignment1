#Let's play with Fibonacci.
n=int(input("enter number of terms:"))
if n<=0:
    print("invalid number")
if n==1:
    print(0)
if n>=2:
    a=0
    b=1
    print(1,end=" ")
    for i in range (2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
#Send word to mirror dimension.
word=input("enter your word: ")
print(word[-1::-1])

#Don't go outside in odd days.
Days=(1,2,3,4,5,6,7,8,9,10,11,12,13)
even=0
odd=0
for i in Days:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print('Total number of even days: ',even)
print('Total number of odd days: ',odd ,end='')
print(' , Do not go outside.')
