import argparse
import fileinput
import random
import re

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mapping", help="declares the mapping of digits", required=True)
parser.add_argument("-s", "--step", help="declares the step going through the map (default=1) [must be odd]")

args = parser.parse_args()
mapping = args.mapping
step = 1

if args.step:
    step = args.step

if len(mapping) != 10:
    print("Please enter map of length 10 for all digits")
    exit(1)

# iterate through all lines of the file
for line in fileinput.input():
    match = re.search(r"^\d{7,8}", line)

    modifier = random.randrange(0,10)

    # if there's a match, replace the id with the scrambled id
    if match != None:
        id = list(match.string.split()[0])
        for index, value in enumerate(id):
            if value != "/":
                # id[index] = str((int(value) + 2) % 10)
                id[index] = mapping[(int(value) + modifier) % 10]
                modifier = (modifier+step) % 10
            else:
                break
        id = "".join(id)
        new_line = line.replace(line.split()[0], str(id))

        # write to standard output
        print(new_line)
