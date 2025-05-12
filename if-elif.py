# Task 1
# m1 = int(input("Enter marks of phy: "))
# m2 = int(input("Enter marks of math: "))
# m3 = int(input("Enter marks of che: "))

# obtmarks = m1 + m2 + m3

# percentage = (obtmarks / 300) * 100

# if (percentage > 33 and m1 >= 33 and m2 >= 33 and m3 >= 33):
#     print("Congratulations! You are pass with good Numbers with percentage:", + percentage)
# elif(percentage == 33 and m1 >= 33 and m2 >= 33 and m3 >= 33):
#     print("You are just pass with percentage: ", + percentage)
# else:
#     print("You are failed with percentage:", + percentage)

# Task 2 - Spam checker
# p1 = "Click This"
# p2 = "Click Now"
# p3 = "Subscribe Now"
# p4 = "Buy Now"

# message = input("Enter your comment: ")

# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("This comment is spam")
# else:
#     print("This comment is not spam")

my_list = ["jam", "spoon", "salt", "sugar"]

your_input = input("You Input: ")

if(your_input in my_list):
    print(your_input, " is in the list")
else: 
    print(your_input, " is not in the list")
