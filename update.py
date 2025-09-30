
TARGET_DIR = "/Users/hersh/Documents/work"
import os
import shutil
import re

def get_files():
    files = []
    for root, dirs, filenames in os.walk(TARGET_DIR):
        for filename in filenames:
            if re.match(r".*compiled.pdf", filename):
                files.append(os.path.join
                             (root, filename))
    return files   

def copy_files(files):
    for file in files:
        directory = os.path.basename(os.path.dirname(os.path.dirname(file)))
        shutil.copy(file, os.path.join(os.getcwd(), directory + ".pdf"))

files = get_files()
copy_files(files)
