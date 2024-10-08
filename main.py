def powerof4(n):
    count = 0
    
    if n&~(n&(n-1)):
        while (n>1):
         n>>=1
         count=count+1
    if count%2 == 0:
       return True
    else:
       return False
n=int(input("Enter Number: "))
if(powerof4(n)):
    print("Number is power of 4")
else:
    print("Number isnt power of 4")