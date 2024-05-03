import os
import re

# Define the suffixes to remove as an array of strings
trash = [
    ' (OFFICIAL VIDEO)','(OFFICIAL VIDEO)', ' [OFFICIAL VIDEO]',
    ' (OFFICIAL MUSIC VIDEO)','(OFFICIAL MUSIC VIDEO)',
    ' (AUDIO)','(AUDIO)',' (OFFICIAL AUDIO)',
    '(320 kbps)','(128 kbps)','(320)','(128)'
    '(Snap2s.com)', '()'
 ]

# Get a list of all files in the current directory
files = os.listdir('.')

# Loop through the files
for file_name in files:
    # Iterate over each trash string to remove
    for trash_string in trash:
        # Check if the file name contains the trash string
        if trash_string in file_name:
            # Create the new name by removing the trash string
            new_name = re.sub(trash_string, '', new_name, flags=re.IGNORECASE)
            new_name = file_name.replace(trash_string, '')
            # Replace multiple consecutive spaces with a single space
            new_name = re.sub(r'\s+', ' ', new_name)
            new_name = re.sub(r'\s*$', '', new_name)
            # Remove spaces at the end of the final filename string
            new_name = new_name.rstrip()
            # Rename the file
            os.rename(file_name, new_name)
            print(f'Renamed "{file_name}" to "{new_name}"')
            # Break out of the inner loop to avoid unnecessary replacements
            break

#TODO regex: Prod. by and so on
#TODO regex: remove everything that's in braces
