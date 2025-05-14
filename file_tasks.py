# Task 1 - Find either a word present in a file or not
# f = open("poem.txt", encoding="utf-8")
# content = f.read()

# word = "twinkle"

# if word in content:
#     print(f"The '{word}' is in the file")
# else:
#     print(f"The '{word}' is not in the file")

# f.close()

# with open("poem.txt", encoding="utf-8") as f:
#     word = "glaxy"
#     content = f.read()
#     if(word in content):
#         print(f"The '{word}' is in the file")
#     else:
#          print(f"The '{word}' is not in the file")

# Task 2 
import random

def game():
    print("You're playing the game!")
    score = random.randint(1, 64)
    with open("hi_score.txt") as f:
        hiScore = f.read()
        if(hiScore != ""):
            hiScore = int(hiScore)
        else:
            hiScore = 0

    print(f"Your score: {score}")
    if(score > hiScore):
        with open("hi_score.txt", "w") as f:
            f.write(str(score))

    return score

game()