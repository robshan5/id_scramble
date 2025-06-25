import re

import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns

with open("modules/MA101.txt") as file:
    """
    take in file
    read through lines, search for ID
    for each ID, add two to each digit and mod 10
    """
    for line in file:
        id = re.search(r"\d{7, 8}", line)
        if id != None:
            print(id.string.split()[0])
            # for index, value in enumerate(id):
            #     value = (int(value)+2) % 10
            # print(id, end="\n\n")
