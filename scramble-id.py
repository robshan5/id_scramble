import os
import re
import sys
from pathlib import Path


def main():
    """
    take in command line argument
    if it's a directory, iterate through the directory
    if it's a file call changeFile once
    """
    if len(sys.argv) != 2:
        print("Please provide file or directory for the grades")
    else:
        path = Path(sys.argv[1])
        
        # checking if the argument is a file or directory
        if path.is_file():
            output = "scrambled.txt"
            changeFile(path, output)
        elif path.is_dir():
            OUTPUTDIR = "scrambled"
            if not os.path.exists(OUTPUTDIR):
                os.makedirs(OUTPUTDIR)

            # if it's a directory, iterate through all text files
            for file in path.rglob("*.txt"):
                output = OUTPUTDIR.join(file.name)
                changeFile(file, output)
        else:
            print(f"No such file or directory {path}")


# function to itereate through a file and replace the ids with a scrambled version
def changeFile(fileName, outputPath):
    with open(fileName) as file:
        """
        take in file
        read through lines, search for ID
        for each ID, add two to each digit and mod 10
        """
        output = open(outputPath, "w")
        #iterate through all lines of the file
        for line in file:
            match = re.search(r"^\d{7,8}", line)

            # if there's a match, replace the id with the scrambled id
            if match != None:
                id = list(match.string.split()[0])
                for index, value in enumerate(id):
                    if value != "/":
                        id[index] = str((int(value) + 2) % 10)
                    else:
                        break
                id = "".join(id)
                new_line = line.replace(line.split()[0], str(id))

                # write to the new file
                output.write(new_line)
                output.write("\n")
            else:
                output.write(line)

if __name__ == "__main__":
    main()
