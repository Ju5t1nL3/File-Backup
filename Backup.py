"""
Automatically backs up a chosen source folder to a chosen destination folder everyday at 6 pm.
"""

from os import path
import shutil
from datetime import date
import schedule
import time
from tkinter import filedialog

def get_directory():
    """
    Returns the folder directory
    """
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    
    return folder

def copy_folder(source, destination):
    """
    Copies the source directory to the destination directory
    """
    today = date.today()
    dest_dir = path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {destination}")

#starts program
if __name__ == "__main__":
    print("Please choose the folder you would like to copy.")
    source = get_directory()
    print("Please choose the folder you would like to backup in.")
    destination = get_directory()
    schedule.every().day.at("18:00").do(lambda: copy_folder(source,destination))

    while True:
        schedule.run_pending()
        time.sleep(60)