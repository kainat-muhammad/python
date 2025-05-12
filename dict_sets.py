# my_dict = {
#     "kainat": 100,
#     "meerab": 89,
#     "areeza": 78
# }

# print(my_dict.items())

# print(my_dict.keys())
# print(my_dict.values())

# test = my_dict.pop("areeza")
# print(test)
# print(my_dict)

# t2 = my_dict.popitem()
# print(t2)
# print(my_dict)

# print(my_dict)

# t3 = my_dict.update({"areeza": 90})
# print(t3)

# print(my_dict)

# Task 1 
# urdu_to_eng = {
#     "bili": "Cat",
#     "kursi": "chair",
#     "bala": "bat",
#     "keela": "Banana"
# }

# translation = input("Enter word which translation you required: ")
# print(urdu_to_eng[translation])

# Task 2 - display unique numbers
# unique_num = set()
# num1 = input("Enter 1st Num: ")
# num2 = input("Enter 2nd Num: ")
# num3 = input("Enter 3rd Num: ")

# unique_num.add(num1)
# unique_num.add(num2)
# unique_num.add(num3)

# print(unique_num)

# Task - 3
# my_set = {8, "8"}
# print(my_set)

# Task - 4
my_dict = {}
key1 = input("Enter your name: ")
value1 = input("Enter your fav language: ")
my_dict[key1] = value1

key2 = input("Enter your name: ")
value2 = input("Enter your fav language: ")
my_dict[key2] = value2

key3 = input("Enter your name: ")
value3 = input("Enter your fav language: ")
my_dict[key3] = value3

print(my_dict)