"""
                                ╔═════════════════════════════════════════════╗
                                ║             .-') _                          ║
                                ║            (  OO) )                         ║
                                ║          ,(_)----. .---. .-----.            ║
                                ║          |       |/_   |/  -.   \           ║
                                ║          '--.   /  |   |'-' _'  |           ║
                                ║          (_/   /   |   |   |_  <            ║
                                ║           /   /___ |   |.-.  |  |           ║
                                ║          |        ||   |\ `-'   /           ║
                                ║          `--------'`---' `----''     ©2021  ║
                                ╚═════════════════════════════════════════════╝
"""
import argparse, feedparser, os, schedule, time

from feedsearch_crawler import search
from datetime import datetime
from tqdm import tqdm

from unicode import to_precomposed, normalize_tone_marks
from addresses import rss_dict


parser = argparse.ArgumentParser(description='Configs for the crawler.')
parser.add_argument('--path', dest="path", default="./data",
                    help='the path to store crawled data')
parser.add_argument('--time', dest="time", default="11:20",
                    help='the time the crawler will run everyday')

args = parser.parse_args()


def crawl_for_titles(root_url):
    titles = []
    try:
        feeds = search(root_url)
        feed_urls = [feed.serialize()['url'] for feed in feeds]
        for url in tqdm(feed_urls):
            try:
                feed = feedparser.parse(url)
                for entry in feed['entries']:
                    titles.append(normalize_tone_marks(to_precomposed(entry['title'])))
            except Exception:
                print("Cannot parse", url)
    except Exception:
        print("Cannot find rss feeds from", root_url)
    return titles


def crawl_and_write_to_file(rss_dict=rss_dict):
    if not os.path.exists(args.path):
        os.mkdir(args.path)
    print("Starting crawling at", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    tqdm.write("Batch crawling")
    for item in tqdm(rss_dict):
        titles = crawl_for_titles(rss_dict[item])
        with open(args.path + "/" + item + ".txt", 'a+') as f:
            for title in titles:
                f.write(title + "\n")
    print("Finished at", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == '__main__':
    # crawl_and_write_to_file()
    schedule.every().day.at(args.time).do(crawl_and_write_to_file)
    while True:
        schedule.run_pending()
        time.sleep(1)
