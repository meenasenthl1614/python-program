from mmap import MADV_RANDOM


MADV_RANDOM#palindrome

s = input("enter the value:")

reverse = s[::-1 ]

if(s == reverse):
    print("its a palindrome number")
else:
    print("its a not palindrome number")





def palindrome(no):
    new = 0
    while (no != 0):
        new = new + (no % 10)
        new = new * 10
        no = no // 10

    new = new / 10
    return int(new)

n=int(input('Enter the number'))
if n == palindrome(n):
    print(n , "is a palindrome")   
else:
    print(n , "is not a palindrome")  
