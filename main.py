import os
import sys
import re
import argparse


argsParser = argparse.ArgumentParser(
  formatter_class=argparse.RawTextHelpFormatter,
  description='Python script for renaming files by given names or regular expression',
)
argsParser.add_argument('-d', '--directory', action='store', default='', help='path to the directory with files')
argsParser.add_argument('-e', '--extension', action='store', default='', help='files extension for search')
argsParser.add_argument('-r', '--regex', action='store_true', help='use regular expressions')
args = argsParser.parse_args()


def main():
    directory = os.path.abspath(args.directory) # Path to the directory with files
    use_names = not args.regex # Use predefined names or regexes(line 44)
    names = [] # List of names
    files = [] # List of files
    extension = args.extension # Files extension for search


    # Get names
    if use_names:
      try:
          with open(os.path.join(os.getcwd(), 'names')) as f:
              names = list(filter(None, [name.strip() for name in f.readlines()]))
      except FileNotFoundError:
        sys.exit('Error: File with names does not exist')


    # Get files
    try:
        for file in os.listdir(directory):
            if file.endswith(f'.{extension}'):
                files.append(file)
    except FileNotFoundError:
        sys.exit('Error: Folder with files does not exist')


    # Check the number of files
    if len(files) == 0:
      sys.exit(f"""Error: There is nothing to rename. Change directory or specify files extension
       Current directory: '{directory}'
       Current extension: '{extension}'""")


    # Compare the number of files and names
    if use_names:
      if (len(names) != len(files)):
          sys.exit(f'Error: The number of names does not match the number of files({len(files)}/{len(names)})')


    # Rename files
    for i in range(len(files)):
        if use_names:
          new_name = f'{i + 1:02d} - {names[i]}.{extension}'
        else:
          # Add your regex patterns here
          new_name = re.sub(r'', '', files[i])

        old_file = os.path.join(directory, files[i])
        new_file = os.path.join(directory, new_name)

        print(f'Rename: {files[i]} -> {new_name}')
        os.rename(old_file, new_file)


if __name__ == '__main__':
    main()
