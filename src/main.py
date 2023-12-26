import os 

os.chdir(f"{os.getcwd()}/src")
os.mkdir("test")

for i in range(10):
    filename = f"{os.getcwd()}/test/{i}.txt"
    with open(filename, 'w') as f:
        f.write("Hello World!")

 
