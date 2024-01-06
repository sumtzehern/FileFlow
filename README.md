# Automation File Organizer

## Introduction

The **Automation File Organizer** is a Python script designed to streamline the organization of files in the user's Downloads folder. Over time, the Downloads folder can become cluttered with various files, making it challenging to locate specific items. This script automates the process of sorting files into distinct folders based on their types, such as documents, images, software, and others.

## Why Do We Need This?

The need for an organized Downloads folder arises from the common scenario where numerous files accumulate over time, resulting in a disorganized and cluttered space. The **Automation File Organizer** provides a solution to this issue by categorizing files into specific folders, making it easier for users to find and manage their files.

## Features

1. **Automated File Sorting Script**
   - The script is the core component of the **Automation File Organizer**. It categorizes files into different folders based on their types, facilitating a more organized and structured Downloads directory.

2. **Customizable File Types**
   - The script allows users to customize file types for categorization. Currently, it supports three main types: documents, images, and software. However, users can easily extend this by adding more file extensions and categories.

3. **Preservation of Script**
   - To ensure that the script itself is not inadvertently organized into a different folder, it uses the `startswith("_")` condition, keeping the script in the Downloads directory.

## Usage

### Part 1:

1. **Download the Script**
   - Save the Python script, `_download_automation.py`, to your Downloads folder.

2. **Customize File Types (Optional)**
   - The script allows users to customize file types for categorization. Currently, it supports a variety of types:
     - Documents: .doc, .docx, .odt, .pdf, .xls, .xlsx, .ppt, .pptx
     - Images: .jpg, .jpeg, .png, .svg, .gif, .tif, .tiff
     - Software: .exe, .pkg, .dmg
     - Audio: .mp3, .wav, .flac
     - Videos: .mp4, .mov, .avi
     - Archives: .zip, .rar, .tar
     - Spreadsheets: .csv
     - Programming Files: .py, .java, .cpp
   - Users can easily extend this list by adding more file extensions and categories.

3. **Run the Script Manually**
   - Open a terminal.
   - Navigate to the Downloads folder.
   - Create a few folder for your organized file
   - Run the script using the command: `python3 automation.py >>~/Downloads/Log/log.txt`
   - Your Downloads folder should look organized now and the log file will store or log information

## Automating with cron:

**Cron** is a time-based job scheduler in Unix-like operating systems. It allows users to schedule tasks to run periodically at fixed times, dates, or intervals. Here's how you can automate the **Automation File Organizer** script using cron:

1. **View Existing Cron Jobs:**
   ```bash
   crontab -l 
   ```

2. **Edit Cron Jobs:**
   ```bash
   crontab -e 
   ```
   This command opens the user's crontab file for editing, allowing them to add or modify cron jobs.

** Automate the Script to Run Every Hour **
```bash
0 */1 * * * cd ~/Downloads/ && python3 _download_automation.py >>~/Downloads/Log/log.txt
```

** Note: If you encounter any issues running the script, ensure that the correct path to Python3 is set. You can check the path using the following command: **
   ```bash
   which python3
   ```
Additionally, when automating the script with cron, it's crucial to specify the correct Python3 path. You can add the following line at the beginning of your script:
   ```bash
    #!/usr/bin/python3
   ```

# Resources

Here are some helpful resources to explore further on working with files in Python and automation:

1. **Working with Files in Python:**
   - [Real Python - Working with Files in Python](https://realpython.com/working-with-files-in-python/)

2. **Automation in Python - Organizing Files:**
   - [Medium - Automation in Python: Organizing Files](https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)

Feel free to refer to these resources for in-depth information and practical insights into file handling and automation using Python.
