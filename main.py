import os
import sys
import re


def main():
    directory = os.path.abspath('') # Path to the directory with files
    use_names = True # Use predefined names or regexps(line 44)
    names = [] # List of names
    files = [] # List of files
    extension = '' # Files extension for search


    # Get names
    if use_names:
      try:
          with open(os.path.join(os.getcwd(), 'names')) as f:
              names = [name.strip() for name in f.readlines()]
      except FileNotFoundError:
        sys.exit('Error: File with names does not exist')


    # Get files
    try:
        for file in os.listdir(directory):
            if file.endswith(f'.{extension}'):
                files.append(file)
    except FileNotFoundError:
        sys.exit('Error: Folder with files does not exist')


    # Check if size of names and files is equal
    if use_names:
      if (len(names) != len(files)):
          sys.exit('Error: The number of names does not match the number of files')


    # Rename files
    for i in range(len(files)):
        if use_names:
          new_name = f'{i + 1:02d}. {names[i]}.{extension}'
        else:
          # Add your regex patterns here
          new_name = re.sub(r'', '', files[i])

        old_file = os.path.join(directory, files[i])
        new_file = os.path.join(directory, new_name)

        print(f'Rename: {files[i]} -> {new_name}')
        os.rename(old_file, new_file)


if __name__ == '__main__':
    main()
