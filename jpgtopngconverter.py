# jpg to png converter
# Script will only work if initiated through a terminal/shell by passing two command line items - current folder, and new folder explained further below
# Script developed by following Andrei Neagoie's Zero to Mastery course @ Udemy
# Certain tweaks made by myself, Awais Ullah, including adding an image converted counter, and moving the print statement outside of the for loop

import sys
import os
from PIL import Image

img_counter = 0

# grab first and second argument - current folder and new folder location
# These must be passed via CLI when executing this script from terminal
# For windows, enter the FULL file path starting from the partition. E.g. C:\user\username\folder
# This script will not work if the paths do not end with a slash (\ windows, or / for unix)

currentfolder = sys.argv[1]
newfolder = sys.argv[2]

# check if the new folder location exists. if it doesnt, create it
if not os.path.exists(newfolder):
    os.makedirs(newfolder)
else:
    print('Folder already exists - No new folder created')
    pass

# look through current folder and convert images to png. Add +1 to the img_counter global variable for each image converted

for filename in os.listdir(currentfolder):
    img = Image.open(f'{currentfolder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{newfolder}{clean_name}.png', 'png')
    img_counter = img_counter + 1

# take credit and provide user with confirmation that the script ran successfully
print(f'all done, converted {img_counter} images')
