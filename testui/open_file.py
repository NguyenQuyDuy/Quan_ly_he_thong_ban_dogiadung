import os

# Get file path
dirpath = os.path.dirname(__file__)
file_path = os.path.join(dirpath, 'fileoi.txt')

# Open file (mode default: r = Read only)
with open(file_path, 'r') as file:
    print('Open file with default mode.')
    # Read file
    content = file.read()
    print('File content:', content)

# Open file (mode: r+ = Read and Write)
with open(file_path, 'r+') as file:
    print('Open file with Read & Write mode.')
    # Read file
    content = file.read()
    print('File content:', content)

    # Write to file
    file.write("\nAdditional content.")
    file.seek(0)  # Move cursor back to the beginning of the file
    updated_content = file.read()
    print('Updated file content:', updated_content)