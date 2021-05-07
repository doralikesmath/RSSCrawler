echo "Merging text files"
cat ./data/* > corpus.txt
echo "Removing duplicates"
python clean.py
echo "Sorting"
sort corpus.txt > corpus_cleaned.txt
echo "Housekeeping"
rm corpus.txt
mv corpus_cleaned.txt corpus.txt
echo "Task finished"