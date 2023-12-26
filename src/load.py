import os 

project_root = os.getcwd()
print(project_root)

target_folder_name = "target_folder"
target_folder_path = None

for root, dirs, files in os.walk(project_root):
    print(root, dirs, files)