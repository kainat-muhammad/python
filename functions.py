# Task 1 - greater num
# def greater_num():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))
    
#     if a >= b and a >= c:
#         print(f"{a} is the greatest")
#     elif b >= a and b >= c:
#         print(f"{b} is the greatest")
#     else:
#         print(f"{c} is the greatest")

# greater_num()

# Task 2 - Celsius to Fahrenheit 
# def celsius_to_fahrenheit(temp_celsius):
#     temp_fahrenheit = temp_celsius * 9/5 + 32
#     print("Temperature in Fahrenheit: ", round(temp_fahrenheit, 2), "°F")

# temp_celsius = int(input("Enter temperature: "))
# celsius_to_fahrenheit(temp_celsius)

# Task 3 - recursive function
# def sum():
#     if(n == 1):
#         return 1
#     return sum(n-1) + n

# print(sum(4)) 

# Task 4
# def printing_pattern(n):
#     for i in range(n, 0, -1):
#         print("*"*i)

# n = int(input("Enter number: "))
# printing_pattern(n)

# Task 5 - convert inches to cms
def inches_to_cms(n):
    return (f"{n * 2.54} cm")

n = int(input("Enter Num: "))
print(inches_to_cms(n))