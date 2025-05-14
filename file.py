# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()


# with statement - with "with" statement you don't have to explicitly write close
with open("file.txt") as f:
    print(f.read())