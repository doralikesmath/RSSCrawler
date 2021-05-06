# RSSCrawler
A simple crawler for Vietnamese news article titles. The crawler is scheduled to run daily.

To run this, simply run
	
	$ pip install -r requirements.txt
	$ python crawler.py --path "./data" --time "12:00"

To merge all text files into one

	$ cat ./data/* > corpus.txt

To remove duplicates

	$ sort corpus.txt | uniq -u > corpus_cleaned.txt

To run all of these step just once

	$ ./run.sh