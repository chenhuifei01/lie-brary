# ! pip install praw
import praw
import pandas as pd
from datetime import datetime as dt
import lie_brary.scripts.scrap.key as key

# Reddit API
CLIENT_ID = key.CLIENT_ID
SECRET_KEY = key.SECRET_KEY

# read the password file
# with open('account_r.txt', 'r') as f:
#     pw = f.read()

# STEP 1: Authenticate Reddit App
reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = SECRET_KEY,
                     username = key.user,
                     password = key.pw,
                     user_agent = 'test')

# request all posts
subreddit = reddit.subreddit('all')

# Define the search term and the date_since date as variables
# [CHANGE THIS!]
topics = 'safe-t'
keywords = ['Safe-T', 'Purge Law', 'Pretrial Fairness Act']


def scrape_r(keywords) :
    '''
    Scrape posts from Reddit using keywords
    Input: keywords(list)
    Output: csv file
    '''

    lst_post =[]

    # Creation of query method using parameters
    for keyword in keywords:
        for post in subreddit.search(keyword, limit = None):
            if post not in lst_post:
                lst_post.append((post, keyword))

    # Pulling information from Reddit iterable object
    # Creation of dataframe from lst_post
    df_data = []

    for post, keyword in lst_post:
        df_data.append({
            'id_str' : post.id,
            'user.id_str' : post.author_fullname,
            'subreddit' : post.subreddit,
            'title' : post.title,
            'selftext' : post.selftext,
            'text' : post.title + post.selftext,
            'created_at' : dt.fromtimestamp(post.created),
            'upvote_ratio': post.upvote_ratio,
            'ups' : post.ups,
            'downs' : post.downs,
            'score' : post.score,
            'permalink': 'https://www.reddit.com/' + post.permalink,
            'num_comments' : post.num_comments,
            'keyword' : keyword,
            'source' : 'reddit'
        })

    df = pd.DataFrame(df_data)

    #Saving dataframe as a CSV file
    filename = 'reddit_'+topics+dt.now().strftime('%Y%m%d_%H')+'.csv'
    #filename = 'reddit_raw.csv'
    df.to_csv('lie_brary/data/raw_data/' + filename, index=False)
    print('File saved as ', filename, 'at lie_brary/data/raw_data')

    return df


if __name__ == "__main__":
    scrape_r(keywords)

