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
temp_celsius = int(input("Enter temperature: "))
def celsius_to_fahrenheit():
    temp_fahrenheit = temp_celsius * 9/5 + 32
    print("Temperature in Fahrenheit: ", temp_fahrenheit)

celsius_to_fahrenheit()