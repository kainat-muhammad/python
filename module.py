# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# Task 1
# import numpy as np
# arr = np.array([[1, 2, 3], [6, 7, 8, 9]])
# print(arr.shape)

# Task 2
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(joke)
# engine.runAndWait()

# Task 3
import os

def list_directory_contents(path):
    try:
        # Get list of files and directories in the given path
        items = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)




