#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

num = int(input("Enter a number: "))

dif = difference(num)

print("The ans is: "+ str(dif))

#OUTPUT

Enter a number: 23
The ans is: 12 
  
Enter a number: 12
The ans is: 5  
