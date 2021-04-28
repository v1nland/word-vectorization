# word-vectorization

Word vectorization is a project that implements word2vec using tweets datasets

## Installation

First of all, install all dependencies (and its versions):

```sh
pip3 install -r requirements.txt
```

## Use

To use this repository, you need a JSON list file (.jsonl) containing tweets data. There's an example inside the **'data'** folder. To generate this type of files you can use [Hydrator](https://github.com/DocNow/hydrator) based on a tweetsID file.

### Tweets parsing

The first step to generate our w2v model is cleaning and sanitizing the tweets data. The file **'read_jsonl.py'** reads a .JSONL file (defined on **'main.py'**), cleans any non-ascii character and writes a corpus file with only the tweet data.

### Generating w2v model

Once our data is clean, we can use the generated corpus to create and train a word2vec model. The file **'generate_model.py'** reads a .CORPUS file (defined on **'main.py'**), then creates and trains a word2vec model for that corpus.

### Running

This process is encapsulated inside a **'main.py'** file, you can just run the following command:

```sh
python3 main.py
```

### Merging huge datasets

There are cases when we need to merge huge datasets (for example hurricanes and earthquakes). Inside the **'helper'** folder, there is a helper file called **'join_files.py'**. This file reads line by line the files declared inside it (line 3), and writes it to another file. The reading process is made line by line to avoid a memory overflow.

Please note you need your files to be inside the **'data'** folder, and run **'join_files.py'** from the root of the project:

```sh
python3 helper/main.py
```
