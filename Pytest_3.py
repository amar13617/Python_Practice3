#Find average
a_list = [1,2,3,4,5,6]
sm = 0
for i in a_list:
    sm = sm+i
    result = sm/len(a_list)
    
#print(result)

#Python program to check whether the given integer is a multiple of 5
num = 25
if num % 5 == 0:
    print("multiple of 5")
else:
    print("not multiple of 5")

#Python program to check whether the given integer is a multiple of both 5 and 7
num = 42
if ((num % 5 == 0) and (num % 7 == 0)):
    print("yes")
else:
    print("no")

#Python program to find the average of 10 numbers using for loop
sm = 0
for i in range(1,11):
    sm = sm + i
    result = sm /10
#print(result)

#Python program to display the given integer in a reverse manner.
n = 524
rev = 0
while n > 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
#print(rev)

#Python program to display all integers within the range 100-200 whose sum of digits is an even number

#Python program to check whether the given integer is a prime number or not
num = 89
if num > 1:
    for i in range(2, int(num//2)+1):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("prime")

for i in range(10, 30):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                #print("not prime")
                break
        else:
            print(i)
            


