import datetime
import os
# import twint
import pathlib

DATE_START = "2022-12-01" #str(datetime.datetime.today().date() - datetime.timedelta(days=1))
DATA_PATH = pathlib.Path("data/")
DATA_PATH.mkdir(parents=True, exist_ok=True)
# MAX_RESULT = 100
DATE_END = "2023-01-01"
HASHTAG = 'happiness'
JSON_FILENAME = DATA_PATH / str(DATE_START) #str(datetime.datetime.today().date())

def sns_scrape():
    #os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG}" > {JSON_FILENAME}.json')

    # with end date
    os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG} until:{DATE_END}" > {JSON_FILENAME}.json')


if __name__ == "__main__":
    sns_scrape()


# reference
# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# https://github.com/hansheng0512/tweets-scrapping-using-python
# https://github.community/t/can-github-actions-directly-edit-files-in-a-repository/17884/7