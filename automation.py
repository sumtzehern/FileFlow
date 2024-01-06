'''Automation File Organizer'''
#!/usr/bin/python3

import os

from shutil import move

# Directory Path 
user = os.path.basename(os.path.expanduser("~"))
root_directory = '/Users/{}/Downloads/'.format(user)
image_directory = '/Users/{}/Downloads/images/'.format(user)
document_directory = '/Users/{}/Downloads/documents/'.format(user)
other_directory = '/Users/{}/Downloads/others/'.format(user)
software_dir = '/Users/{}/Downloads/softwares/'.format(user)


# Organize the file (doc, img, software)
# Document types
doc = (".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")
# Image type
img = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
# Software Type
software = ('.exe', '.pkg', '.dmg')

def get_non_hidden_files(root_directory):
    return [
        f for f in os.listdir(root_directory) 
        if os.path.isfile(f) and not f.startswith('_') and not f.__eq__(__file__)
    ]

def move_files(files):
    for file in files:
        if file.endswith(doc): # moved fie and overwritten
            move(file, '{}/{}'.format(document_directory, file))
            print('file {} moved to {}'.format(file, document_directory))
        elif file.endswith(img):
            move(file, '{}/{}'.format(image_directory, file))
            print('file {} moved to {}'.format(file, image_directory))
        elif file.endswith(software):
            move(file, '{}/{}'.format(software_dir, file))
            print('file {} moved to {}'.format(file, software_dir))
        else:
            move(file, '{}/{}'.format(other_directory, file))
            print('file {} moved to {}'.format(file, other_directory))

if __name__ == "__main__":
    files = get_non_hidden_files(root_directory)
    move_files(files)