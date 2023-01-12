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

num = 42
if ((num % 5 == 0) and (num % 7 == 0)):
    print("yes")
else:
    print("no")
