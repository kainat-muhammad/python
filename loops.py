
# Task 1 - Print Table using for loop
# tableOf = int(input("Enter number: "))
# for i in range(1, 11):
#     # print("6 * ",i, "=", i * 6)
#     print(f"{tableOf} * {i} = {i * tableOf}")


# Task 2 - Print Table using while loop
# tableOf = int(input("Enter number: "))
# i = 1
# while(i < 11):
#     print(f"{tableOf} * {i} = {i * tableOf}")
#     i += 1

# Task 3 - Prime num or not
# num = int(input("Enter a number: "))

# for i in range(2, num):
#     if(num%i == 0):
#         print("Num is not prime")
#         break
# else:
#     print("Num is prime")

# Task 4 - sum of 1st 5 natural numbers
# total = 0
# for i in range(1, 6):
#     total += i
# print("Sum: ", total)

# Task 5 - find factorial of a number
# factorial = 1
# n = int(input("Enter a number: "))
# for i in range (1, n + 1):
#     factorial *= i
    
# print(f"The factorial of {n} is {factorial}")

# Task 6 - star pattern 
# star = "*"
# n= int(input("Enter num: "))
# for i in range (1, n+1):
#     print(" "* (n-i), end = "")
#     print(star * (2*i-1), end = "")
#     print("")

# Task 7 
'''
***
* *
***
'''

# n = int(input("Enter num:"))
# star = "*"
# for i in range(1, n+1):
#     if(i==1 or i == n):
#         print(star*n, end="")
#     else:
#         print(star, end="")
#         print(" "*(n-2) , end="")
#         print(star, end="")
#     print("")

# We can also do the above program like this
# n = int(input("Enter num: "))
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n)
#     else:
#         print("*" + " " * (n - 2) + "*")

n = int(input("Enter num: "))
for i in range(10, 0, -1):
    print(f"{n} * {i} = {n*i}")
