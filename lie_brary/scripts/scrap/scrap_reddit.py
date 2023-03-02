# ! pip install praw
import praw
import pandas as pd
import datetime as dt

# Reddit API
CLIENT_ID = 'shyhwdBJkuFVOeR-cI-piw'
SECRET_KEY = 'A984oPGBir78gCC8Ce8RBe1X9K3chg'

# read the password file
with open('account_r.txt', 'r') as f:
    pw = f.read()

# STEP 1: Authenticate Reddit App
reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = SECRET_KEY,
                     username = 'chenhuifei1',
                     password = pw,
                     user_agent = 'test')

# request all posts
subreddit = reddit.subreddit('all')

# Define the search term and the date_since date as variables 
# [CHANGE THIS!]
topics = 'safe-t'
keywords = ['Safe-T', 'Purge Law', 'Pretrial Fairness Act']


def scrape(keywords) : 
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
    df = pd.DataFrame()

    for post, keyword in lst_post:
        df = df.append({
        'id_str' : post.id,
        'user.id_str' : post.author_fullname,
        'subreddit' : post.subreddit,
        'title' : post.title,
        'selftext' : post.selftext,
        'text' : post.title + post.selftext,
        'created_at' : dt.datetime.fromtimestamp(post.created),
        'upvote_ratio': post.upvote_ratio,
        'ups' : post.ups,
        'downs' : post.downs,
        'score' : post.score,
        'permalink': 'https://www.reddit.com/' + post.permalink,
        'num_comments' : post.num_comments,
        'keyword' : keyword
    }, ignore_index = True)

    # Saving dataframe as a CSV file
    filename = 'reddit_'+topics+dt.now().strftime('%Y%m%d_%H')+'.csv'
    df.to_csv(filename)
    print('File saved as ', filename)

    return None


if __name__ == "__main__":
    scrape(keywords)



'''
The keys to pull the data
For example, 'post.title ' will get the title of the post

keys = ['approved_at_utc', 
        'subreddit', 
        'selftext', 
        'author_fullname', 
        'saved', 
        'mod_reason_title', 
        'gilded', 
        'clicked', 
        'title', 
        'link_flair_richtext', 
        'subreddit_name_prefixed', 
        'hidden', 
        'pwls', 
        'link_flair_css_class', 
        'downs', 
        'thumbnail_height', 
        'top_awarded_type', 
        'hide_score', 
        'name', 
        'quarantine', 
        'link_flair_text_color', 
        'upvote_ratio', 
        'author_flair_background_color', 
        'subreddit_type', 
        'ups', 
        'total_awards_received', 
        'media_embed', 
        'thumbnail_width', 
        'author_flair_template_id', 
        'is_original_content', 
        'user_reports', 
        'secure_media', 
        'is_reddit_media_domain', 
        'is_meta', 
        'category', 
        'secure_media_embed', 
        'link_flair_text', 
        'can_mod_post', 
        'score', 
        'approved_by', 
        'is_created_from_ads_ui', 
        'author_premium', 
        'thumbnail', 
        'edited', 
        'author_flair_css_class', 
        'author_flair_richtext', 
        'gildings', 
        'post_hint', 
        'content_categories', 
        'is_self', 
        'mod_note', 
        'created', 
        'link_flair_type', 
        'wls', 
        'removed_by_category', 
        'banned_by', 
        'author_flair_type', 
        'domain', 
        'allow_live_comments', 
        'selftext_html', 
        'likes', 
        'suggested_sort', 
        'banned_at_utc', 
        'url_overridden_by_dest', 
        'view_count', 
        'archived', 
        'no_follow', 
        'is_crosspostable', 
        'pinned', 
        'over_18', 
        'preview', 
        'all_awardings', 
        'awarders', 
        'media_only', 
        'can_gild', 
        'spoiler', 
        'locked', 
        'author_flair_text', 
        'treatment_tags', 
        'visited', 
        'removed_by', 
        'num_reports', 
        'distinguished', 
        'subreddit_id', 
        'author_is_blocked', 
        'mod_reason_by', 
        'removal_reason', 
        'link_flair_background_color', 
        'id', 
        'is_robot_indexable', 
        'report_reasons', 
        'author', 
        'discussion_type', 
        'num_comments', 
        'send_replies', 
        'whitelist_status', 
        'contest_mode', 
        'mod_reports', 
        'author_patreon_flair', 
        'author_flair_text_color', 
        'permalink', 
        'parent_whitelist_status', 
        'stickied', 
        'url', 
        'subreddit_subscribers', 
        'created_utc', 
        'num_crossposts', 
        'media', 
        'is_video']
'''

'''
topics = 'health_en'
lst_keywords = ['damar hamlin + vaccine', 
                'mRNa vaccine', 
                'the jab', 
                'anastasia weaver', 
                'died suddenly', 
                'christian eriksen', 
                'vaers', 
                'vaccine + alumnium', 
                'vaccine + mercury', 
                'vaccine injury', 
                'vaccine sterile', 
                'vaccine ICU', 
                'vaxx', 
                'vac death']

topics = 'health_sp'
lst_keywords = ['vacuna', 
                '#COVID19', 
                'ARNm', 
                'vacuna & embaracada', 
                'ARNm & cáncer']
'''

