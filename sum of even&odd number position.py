 #Find the difference in sum of odd and even digit position in a given number

n = int(input("Enter the number:"))
c = 0
l = []
even = 0
odd = 0
while(n > 0):
    r = n % 10
    l.append(r)
    n = n//10
for i in range(len(l)):
    if(i % 2 == 0):
        odd = odd + l[i]
    else:
        even = even + l[i]
dif = odd - even
print("The differnce in position : ",dif)                