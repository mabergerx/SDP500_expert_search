# ============================================================================

# These functions were used to convert the less usable .txt OAG files to .json
# files, for further processing.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import gc

files = ["mag_papers_0.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("0.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_1.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("1.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_2.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("2.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_3.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("3.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_4.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("4.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_5.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("5.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_6.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("6.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_7.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("7.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_8.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("8.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_9.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("9.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_10.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("10.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_11.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("11.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_12.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("12.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_13.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("13.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_14.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("14.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_15.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("15.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_16.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("16.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_17.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("17.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_18.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("18.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_19.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("19.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_20.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("20.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_21.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("21.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_22.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("22.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_23.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("23.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_24.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("24.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_25.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("25.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_26.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("26.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_27.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("27.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_28.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("28.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_29.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("29.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_30.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("30.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_31.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("31.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_32.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("32.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines


files = ["mag_papers_33.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("33.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_34.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("34.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_35.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("35.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_36.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("36.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_37.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("37.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()

files = ["mag_papers_38.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("38.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_39.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("39.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_40.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("40.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()


files = ["mag_papers_41.txt"]

all_lines = []

for file in files:
    with open(file, "r") as f:
        single_lines = f.readlines()
        all_lines.extend(single_lines)
        del single_lines
        gc.collect()
    print("File", file, "is done.")

with open("41.json", "a") as of:
    #of.write("[")
    for line in all_lines:
        of.write(line)
    #of.write("]")

del all_lines
gc.collect()