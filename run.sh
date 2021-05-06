python crawler.py --crawl_once True
echo "Merging text files"
cat ./data/* > corpus.txt
echo "Removing duplicates and sorting"
sort corpus.txt | uniq -u > corpus_cleaned.txt
echo "Housekeeping"
rm corpus.txt
mv corpus_cleaned.txt corpus.txt
echo "Task finished"