import json, csv, argparse, os, urllib.request
import pandas as pd 
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--clean_dialog_file', required=True)
    parser.add_argument('-o', '--word_counts_json', required=True)
    args = parser.parse_args()

    # open outfile, check it's path and create dirs if necessary
    outfile = args.word_counts_json
    if not os.path.dirname(outfile) == "":
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
    outfile = open(outfile, 'w')

    wcounts = count_word(args.clean_dialog_file)
    
    # write & close files
    outfile.write(json.dumps(wcounts, indent=4))
    outfile.close()


def count_word(dialog_file):
    # store all stopwords into a list
    stopwords = []
    f = urllib.request.urlopen("https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt")
    for line in f:
        line = line.decode('utf-8')
        if not line.startswith("#"):
            stopwords.append(line.rstrip())

    # word counts json structure
    wcounts = {
        "twilight sparkle": {},
        "applejack": {},
        "rarity": {},
        "pinkie pie": {},
        "rainbow dash": {},
        "fluttershy": {},
        "all": {}
    }

    # count words
    df = pd.read_csv(dialog_file)
    for row in df.itertuples():
        for pony in wcounts:
            if pony == "all":
                break
            if pony == row.pony.lower():
                parse_dialog(wcounts, pony, row.dialog, stopwords)


    # filter out words with occurrence < 5
    remove_words = []
    for word in wcounts["all"]:
        if wcounts["all"][word] < 5:
            remove_words.append(word)
    
    for pony in wcounts:
        for word in wcounts[pony].copy():
            if word in remove_words:
                del wcounts[pony][word]

    del wcounts["all"]

    return wcounts



def parse_dialog(wcounts, pony, dialog, stopwords):
    specials = "()[],-.?!:;#&"
    for c in specials:
        dialog = dialog.replace(c, " ")

    for word in dialog.split():
        word = word.lower()
        if not word in stopwords and word.isalpha():
            if word in wcounts[pony]:
                wcounts[pony][word] += 1
            else:
                wcounts[pony][word] = 1

            if word in wcounts["all"]:
                wcounts["all"][word] += 1
            else:
                wcounts["all"][word] = 1


if __name__ == "__main__":
    main()