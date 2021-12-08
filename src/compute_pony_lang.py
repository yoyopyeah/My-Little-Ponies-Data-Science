import argparse, json, sys, math
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--pony_counts_json', required=True)
    parser.add_argument('-n', '--num_words', required=True)
    args = parser.parse_args()

    wcounts = json.load(open(args.pony_counts_json))
    num_words = int(args.num_words)

    data = analyze_lang(wcounts, num_words)
    json.dump(data, sys.stdout, indent=4)


def analyze_lang(wcounts, num_words):
    data = {
        "twilight sparkle": [],
        "applejack": [],
        "rarity": [],
        "pinkie pie": [],
        "rainbow dash": [],
        "fluttershy": []
    }

    # get words sorted by tfidf in dataframe
    for pony in wcounts:
        df = pd.DataFrame(columns = ["word", "tfidf"])

        for word in wcounts[pony]:
            value = tfidf(word, pony, wcounts)
            df.loc[len(df)] = [word, value]
        df = df.sort_values(by=['tfidf'], ascending=False)

        i = 0
        if len(df) < num_words:
            num_words = len(df)
        while i < num_words:
            data[pony].append(df.iloc[i]['word'])
            i += 1

    return data



def tfidf(w, pony, json):
    # json = json.loads(script)
    # tf = the number of times pony uses the word w
    tf = json[pony][w] 
    
    # idf = log(total number of ponies / number of ponies that use the word w)
    count = 0
    for pony in json:
        if w in json[pony]:
            count += 1
    idf = math.log((len(json) / count), 10)

    return tf * idf


if __name__ == "__main__":
    main()