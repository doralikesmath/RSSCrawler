# RSSCrawler
A simple crawler for Vietnamese news article titles. The crawler is scheduled to run daily.

To run this, simply run
	
	$ pip install -r requirements.txt
	$ python crawler.py --path "./data" --time "12:00"

To run the crawler just once to generate a small corpus

	$ ./run.sh