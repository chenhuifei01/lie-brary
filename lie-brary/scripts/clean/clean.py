import pandas as pd
from ..scrap.scrap_twitter import scrape_t # changed the path and name
from datetime import datetime


def clean(old_scrape_filename, new_scrape_filename):
    """
    Cleaning twitter csv file to remove duplicate tweets that occur between
    different scaping times

    Inputs:
        old_scrape_filename: previous scrape of tweets
        new_scrape_filename: latest scrape of tweets
    
    Returns -- consolidated updated csv
    """
    old_scape = pd.read_csv(old_scrape_filename)
    new_scrape = pd.read_csv(new_scrape_filename)

    #merging the old scrape and new scrape tweets
    updated_tweets = pd.concat([old_scape, new_scrape])

    #dropping duplicates
    updated_tweets.drop_duplicates(keep=False)

    filename = 'cleaned_tweets_'+ datetime.now().strftime('%Y%m%d_%H')\
                +'.csv'

    updated_tweets.to_csv(filename, columns= id_str, text,\
            in_reply_to_status_id_str, user.id_str, user.created_at, \
            user.name, user.screen_name, keyword)

    print(f"Duplicates tweets were removed. Please see updated tweets in \
            {filename} ")
    
    return None