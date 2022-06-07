# Count files
import os

print(os.getcwd())

for count in range(1, 1921): # for all files from 1 to 1921
    if not os.path.isfile(f"{count}.png"):
        print(f"{count}.png does not exist!")

print("Done!")