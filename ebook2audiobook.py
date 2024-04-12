import os
import re
import getpass

#gets the user 
user = getpass.getuser()
# Replace 'folder_path' with the path to your folder containing .epub files
folder_path = '/home/'+user+'/Documents/Audiobook/'

def remove_invalid_characters(filename):
    # Define a regular expression to match invalid characters
    invalid_chars_regex = r'[<>:"/\\|?*\x00-\x1F\x7F\s]+'

    # Replace invalid characters with underscores
    cleaned_filename = re.sub(invalid_chars_regex, '_', filename)

    return cleaned_filename

def rename_epub_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    for filename in files:
        if filename.endswith('.epub'):
            # Remove invalid characters from the filename
            cleaned_filename = remove_invalid_characters(filename)

            # Rename the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, cleaned_filename)

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{cleaned_filename}'")

def delete_epub_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    for filename in files:
        if filename.endswith('.epub'):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted '{filename}'")


def voiceaudiobook():
    for filename in os.listdir(folder_path):
        if filename.endswith(".epub"):
            os.system('/home/'+user+'/.local/bin/epub2tts ~/Documents/Audiobook/'+filename+' --engine edge --speaker en-US-AvaNeural --sayparts')


# Call the function to remove .epub files
        


# clean the epubs first 
rename_epub_files(folder_path)
# then run epub2tts
voiceaudiobook()
#deletes the ebpubs 
delete_epub_files(folder_path)
#remove_epub_files(folder_path)    