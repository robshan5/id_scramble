import fileinput
import re

# iterate through all lines of the file
for line in fileinput.input():
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

        # write to standard output
        print(new_line)
