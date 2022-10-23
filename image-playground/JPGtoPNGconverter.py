import sys
import os
from PIL import Image

# Grab the first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# Check if new folder exist, if not create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Loop through the Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')

    # Remove file type and split filename
    remove_fileType = os.path.splitext(filename)[0]
    print(remove_fileType)

    # Save in newly created folder
    img.save(f'{output_folder}{remove_fileType}.png', 'png')
    print(f'{filename} converted!')



