import os
os.mkdir("my_directory")

directory = os.getcwd()
files = os.listdir(directory)
print(files)

py= [file for file in files if file.endswith(".py")]
print(py)

file = "example.py"
if os.path.exists(file):
    os.remove(file)
    print(f"{file} has been removed.")
else:
    print(f"{file} does not exist.")