import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def rename_files(folder_path, text_to_remove):
    try:
        files = os.listdir(folder_path)
        for file_name in files:
            if text_to_remove in file_name:
                new_name = file_name.replace(text_to_remove, '')
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
        print("Files renamed successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        print("Folder selection canceled.")
        return

    text_to_remove = simpledialog.askstring("Text to Remove", "Enter text to remove from file names:")
    if not text_to_remove:
        print("Text input canceled.")
        return

    confirmation = simpledialog.askstring("Confirmation", f"Are you sure you want to remove '{text_to_remove}' from all file names in {folder_path}? (yes/no):")
    if confirmation and confirmation.lower() == 'yes':
        rename_files(folder_path, text_to_remove)
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
