import tkinter as tk
from tkinter import font
import os
from utils import get_project_root

window = tk.Tk()

# Constants
PROJECT_ROOT = get_project_root()

# Fonts
bold_font = font.Font(weight="bold")



# Main Frames
frame1 = tk.Frame(master=window, width=1400, height=500)
frame1.pack()

frame2 = tk.Frame(master=window, width=1400, height=200, bg="blue")
frame2.pack()

# Sub Frames
frame1_sub1 = tk.Frame(master=frame1, width=1000, height=500, bg="green")
frame1_sub1.pack(fill=tk.Y, side=tk.LEFT)

frame1_sub2 = tk.Frame(master=frame1, width=400, height=500, bg="white")
frame1_sub2.pack_propagate(flag=False)
frame1_sub2.pack(fill=tk.Y, side=tk.RIGHT)

# frame1_sub2
# Title
title_font = font.Font(family="Helvetica", size=20, weight="bold")
title = tk.Label(master=frame1_sub2, text="Annonator", width=10, font=title_font, bg="white", fg="black")
title.pack(fill=tk.X, pady=10)

# Project Root
project_root_frame = tk.Frame(master=frame1_sub2, bg="white", width=400)

project_root = tk.Label(master=project_root_frame, text="Project Root: ", bg="white", fg="black", font=bold_font)
project_root_path = tk.Label(master=project_root_frame, text=f"/{PROJECT_ROOT}", bg="white", fg="black")

project_root_frame.pack(padx=10, pady=10, fill=tk.X)
project_root.pack(fill=tk.Y, side=tk.LEFT)
project_root_path.pack(fill=tk.Y)

# Target Folder Name
target_folder_frame = tk.Frame(master=frame1_sub2, bg="white", width=400)

target_folder_name = tk.Label(master=target_folder_frame, text="Target Folder Name: ", bg="white", fg="black", font=bold_font)
target_folder_name_entry = tk.Entry(master=target_folder_frame, width=15, bg="white", fg="black")
print(target_folder_name_entry.get())

target_folder_frame.pack(padx=10, pady=10, fill=tk.X)
target_folder_name.pack(fill=tk.Y, side=tk.LEFT)
target_folder_name_entry.pack(fill=tk.X)

# List Files in Target Folder
list_files_frame = tk.Frame(master=frame1_sub2, bg="white", width=400)
search_button = tk.Button(master=list_files_frame, text="Search", width=10, bg="white", fg="black")

list_files_frame.pack(padx=10, pady=10, fill=tk.X)
search_button.pack(fill=tk.X)


window.mainloop()