# word-vectorization

Word vectorization is a project that implements word2vec using tweets datasets

## Installation

First of all, install all dependencies (and its versions):

```sh
# default pip3 use
pip3 install -r requirements.txt

# to avoid any problem, run:
sudo -H python3 -m pip install -r requirements.txt
```

## Use

To use this repository, you need a JSON list file (.jsonl) containing tweets data. There's an example inside the **'data'** folder. To generate this type of files you can use [Hydrator](https://github.com/DocNow/hydrator) based on a tweetsID file.

### Tweets parsing

The first step to generate our w2v model is cleaning and sanitizing the tweets data. The file **'read_jsonl.py'** reads a .JSONL file (defined inside the file), cleans any non-ascii character and writes a corpus file with only the tweet data. To use this file, run the following command:

```sh
python3 read_jsonl.py
```

### Generating w2v model

Once our data is clean, we can use the generated corpus to create and train a word2vec model. The file **'generate_model.py'** reads a .CORPUS file (defined inside the file), then creates and trains a word2vec model for that corpus. To use this file, run the following command:

```sh
python3 generate_model.py
```

### Creating train sets for neural networks

If you're working with another neural network and need to create a training set (for supervised training, for example), you can use the **'build_train_set.py'** file. This file defines a list of corpus files inside it (for example, ["earthquake", "hurricane"]) and selects the first K tweets (also defined inside as TWEETS_NUMBER) of each file, then generates a JSON file with the type and the content of the row. Please remember to have your files inside the **'corpus'** folder, and name your files **'{file_name}.corpus'**. To use this file, run the following command:

Please note that you NEED to use CORPUS FILES, because the word2vec model was created using these files.

```sh
python3 build_train_set.py
```

### Running model API for model querying

This repository provides a simple REST API to query our generated model. This process is encapsulated inside the **'main.py'** file. The API was made with FastAPI. To start the server, run the following command:

```sh
uvicorn main:app --reload
```

### Merging huge datasets

There are cases when we need to merge huge datasets (for example hurricanes and earthquakes). Inside the **'helper'** folder, there is a helper file called **'join_files.py'**. This file reads line by line the files declared inside it (line 3), and writes it to another file. The reading process is made line by line to avoid a memory overflow.

Please note you need your files to be inside the **'data'** folder, and run **'join_files.py'** from the root of the project:

```sh
python3 helper/join_files.py
```

### Testing with smaller datasets

If you already have a huge dataset and want to test functionality with a sub-set of that, you can use **'first_k_tweets.py'** inside the **'helper'** folder. The program takes the first K lines (declared on a constant inside the file) and writes it to another file.

Please note you need your files to be inside the **'data'** folder, and run **'first_k_tweets.py'** from the root of the project:

```sh
python3 helper/first_k_tweets.py
```
