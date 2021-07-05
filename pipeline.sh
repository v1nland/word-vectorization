# run as: sh pipeline.sh {dataset_1} {dataset_2} {words_per_tweet} {lines_per_batch}
# example: sh pipeline.sh nepal harvey-irma-maria 16

FILE_1=$1
FILE_2=$2
BOTH_FILES=$1_$2
WORD_PER_TWEET=$3
LINES_PER_BATCH=$4

# join both files
# python3 join_files.py \[\'$FILE_1\',\'$FILE_2\'\]

# # generate corpus individually
# python3 read_jsonl.py $FILE_1 $FILE_1
# python3 read_jsonl.py $FILE_2 $FILE_2
# python3 read_jsonl.py $BOTH_FILES $BOTH_FILES

# # generate w2v model
# python3 generate_model.py $BOTH_FILES $BOTH_FILES

# # build whole set with types
# # use 0 as parameter to read all lines
# python3 build_set.py \[\'$FILE_1\',\'$FILE_2\'\] 0

# # shuffle the generated set
# python3 shuffle_set.py $BOTH_FILES $BOTH_FILES

# retrieve the vector form of the shuffled_set
python3 vectorizate_set.py $BOTH_FILES $BOTH_FILES $BOTH_FILES $WORD_PER_TWEET

# make batches from the shuffled set
mkdir vectorizated_shuffled_set/${BOTH_FILES}_batches
gsplit -d -a 2 -l $LINES_PER_BATCH vectorizated_shuffled_set/$BOTH_FILES.vectorizated_shuffled_set vectorizated_shuffled_set/${BOTH_FILES}_batches/
