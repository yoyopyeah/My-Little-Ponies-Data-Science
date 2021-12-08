# My Little Ponies Data Science Project

    Performs data collection, filtering, reformatting, and analysis on 36860 speech acts from My Little Ponies [transcript](https://www.kaggle.com/liury123/my-little-pony-transcript). Analyzed data on individual and global scales, and examined the speech features of key characters.


## Set up
* Python 3.6 or higher
* `pip` - see instructions [here](https://packaging.python.org/tutorials/installing-packages/)
* Other packages - run at the project root:
```
pip3 install -r requirements.txt
```

## Project structure
```
├── data
    ├── clean_dialog.csv
    ├── word_counts.json
├── src
    ├── dialog_analysis.py
    ├── compile_word_counts.py
    ├── compute_pony_lang.py
    ├── build_interaction_network.py
    ├── compute_network_stats.py
├── test
    ├── ...
├── README.md
├── requirements.txt
```
### Dialog analysis
* dialog_analysis.py: counts the number of speech acts of 6 main ponies and calculates their verbosity, outputs result into structured JSON file. 
    - Run with `python3 dialog_analysis.py -o output.json clean_dialog.csv`
### Compile word counts
* compile_word_counts.py: computes word counts for each pony from all episodes of MLP with elimination of [stopwords](https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt), outputs result into structured JSON file. 
    - Run with `python3 compile_word_counts.py -o <word_counts_json> -d <clean_dialog.csv file>`
### TF-IDF score analysis
* compute_pony_lang.py: compute the \<num_words\> for each pony that has the highest TF-IDF score, outputs result in JSON to stdout. 
    - Run with `python3 compute_pony_lang.py -c <pony_counts.json> -n <num_words>`
### Build & analyze interaction network
*  build_interaction_network.py: create conversation interaction among top 101 most frequent characters, outputs result into structured JSON file. 
    - Run with `python3 build_interaction_network.py -i /path/to/<script_input.csv> -o /path/to/<interaction_network.json>`
* compute_network_stats.py: utilize networkx and analyze the connectiveness of characters from multiple perspectives, outputs result into structured JSON file. 
    - Run with `python3 compute_network_stats.py -i /path/to/<interaction_network.json> -o /path/to/<stats.json>`
### Unit tests
* Scripts under test/ performing unit tests, ensure the proper running of the programs.
    - Run with `python3 -m unittest`



## Reference
The project inspired by McGill Fall 2021 COMP 598 Data Science by Professor Ruths.
Transcript clean_dialog.csv retrieved at https://www.kaggle.com/liury123/my-little-pony-transcript