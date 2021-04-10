def lcmFunc(m,n):

    lcm = 0
    z=m*n
    
    for i in range(m,z+1):
        if i%m == 0 and i%n == 0:
            lcm = i
            break          
                
    return lcm    

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

lcm = lcmFunc(a,b)

print("The lcm is: "+ str(lcm))