# Back Up

import os
import shutil
from datetime import datetime
import schedule
import time

source_dir = "C:\\Users\\hp\\Desktop\\test_docs"
destination_dir = "C:\\Users\\hp\\Desktop\\test_backup"


def copy_folder_to_directory(source, dest):
    today = datetime.today()
    dest_dir = os.path.join(dest, today.strftime("%Y-%m-%d"))  

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("12:00").do(copy_folder_to_directory, source_dir, destination_dir)

while True:
    schedule.run_pending()
    time.sleep(60)

