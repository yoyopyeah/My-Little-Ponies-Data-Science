import json
import csv
import sys

# base structure
base = {
    "count": {
        "twilight sparkle": 0,
        "applejack": 0,
        "rarity": 0,
        "pinkie pie": 0,
        "rainbow dash": 0,
        "fluttershy": 0
    },
    "verbosity": {
        "twilight sparkle": 0,
        "applejack": 0,
        "rarity": 0,
        "pinkie pie": 0,
        "rainbow dash": 0,
        "fluttershy": 0
    } 
}

total = -1

with open (sys.argv[3]) as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        total += 1
        for pony in base["count"]:
            if pony == row[2].lower():
                base["count"][pony] += 1
    for pony in base["verbosity"]:
        base["verbosity"][pony] = round(base["count"][pony] / total, 2)

# write to output file
f = open(sys.argv[2], "w")
f.write(json.dumps(base, indent=1))
f.close()

