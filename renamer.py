# Python program to rename all files with ex_ to not include ex_
import os

print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    if "ex_" in f_name:
        f_name = f_name.replace("ex_", "")
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
    else:
        print(f"{f_name} doesn't contain 'ex_'")
print("Removed all ex_ from names. Done!")