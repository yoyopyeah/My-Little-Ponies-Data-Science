# My Little Ponies Data Science Project

Performs data collection and analyzes 36860 speech acts from My Little Ponies [transcript](https://www.kaggle.com/liury123/my-little-pony-transcript). 

## Project structure
```
├── data
    ├── clean_dialog.csv
    ├── word_counts.json
├── scripts
    ├── 
├── src
    ├── dialog_analysis.py
    ├── compile_word_counts.py
    ├── compute_pony_lang.py
    ├──
├── test
    ├── fixtures
        ├── ...
    ├── 
```
### Dialog analysis
- dialog_analysis.py: counts the number of speech acts of 6 main ponies and calculates their verbosity, outputs result into structured json file. 
- Run with `python3 dialog_analysis.py -o output.json clean_dialog.csv`
### Compile word counts
- compile_word_counts.py: computes word counts for each pony from all episodes of MLP with elimination of [stopwords](https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt), outputs result into structured json file. 
- Run with `python3 compile_word_counts.py -o <word_counts_json> -d <clean_dialog.csv file>`
### TF-IDF score analysis
- compute_pony_lang.py: compute the <num_words> for each pony that has the highest TF-IDF score, outputs result in json to stdout. 
- Run with `python3 compute_pony_lang.py -c <pony_counts.json> -n <num_words>`
### Unit tests
- Scripts under test/ performing unit test, ensure the proper running of the data.
- Run with `python3 -m unittest`


## Set up
* Python 3
* `pip` - see instructions [here](https://packaging.python.org/tutorials/installing-packages/)
* Other packages - run at the project root:
```
pip install -r requirements.txt
```

## Reference
The project inspired by McGill Fall 2021 COMP 598 Data Science by Professor Ruths.
Transcript clean_dialog.csv retrieved at https://www.kaggle.com/liury123/my-little-pony-transcript