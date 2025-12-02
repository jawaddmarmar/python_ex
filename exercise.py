#exercise 1
name=input("insert your name:")
age=input("insert your age:")
print(f'The user {name} is {age} years old')

#exercise 2
nb=input("insert a number:")

nums=int(nb) % 2
nums2=int(nb) % 4
if nums == 0:
    print("this is even number")
elif nums2 == 0:
    print("this number can be divided by 4")
else:
    print("this is an odd number")


num=int(input("insert the first number:"))
check=int(input("insert the second number:"))

if  num % check == 0:
    print(f'the remain of {num} divided by {check} is 0')
else:
    print(f'the remain of {num} divided by {check} is not 0')