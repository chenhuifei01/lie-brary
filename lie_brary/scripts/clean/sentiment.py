import pandas as pd
import numpy as np
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
#from tqdm.notebook import tqdm
from datetime import datetime


sia = SentimentIntensityAnalyzer()
# example
# sia.polarity_scores('I am so happy!')
# Output: {'neg': 0.0, 'neu': 0.318, 'pos': 0.682, 'compound': 0.6468}

def sentiment_analysis(df):
    '''
    Analyze the sentiment according to the text of a post
    Input: dataframe
    Return: dataframe with sentiment columns
    '''
    # Run the polarity score on the entire dataset
    res = {}
    for i in range(len(df)):
        text = df.iloc[i]['text']
        myid = df.iloc[i]['id_str']
        res[myid] = sia.polarity_scores(text)
    vaders = pd.DataFrame(res).T
    vaders = vaders.reset_index().rename(columns = {'index':'id_str'})
    vaders = vaders.merge(df, how = 'left')
    return vaders

def clean_time_t(x):
    '''
    Change the date format from '2023-02-05 22:51:19+00:00'
    to '2023-02-05 22:51:19' for twitter data
    Input: datetime
    Output: datetime
    '''
    #dt_obj = datetime.strptime(x,"%Y-%m-%d %H:%M:%S%z")
    return datetime.strftime(x, "%Y-%m-%d %H:%M:%S")


def sentiment_define(x):
    '''
    Define the compound grades into three sentiments,
    positive, neutral, and negative.
    Input(float): compound grade
    Return(str): positive, neutral, and negative
    '''
    # positive range: 0.3333 ~ 1
    # neutral range: -0.3333 ~ 0.3333
    # negative range: -1 ~ -0.3333
    up_b = 1
    lw_b = -1
    devided = 3
    threshold = (up_b - lw_b)/devided
    if x >= (up_b - threshold):
        return 'positive'
    elif x <= (lw_b + threshold):
        return 'negative'
    else:
        return 'neutral'


def extract_col(df, source):
    '''
    Extract the columns to output the Cleaned_data
    Inputs:
        df(pandas dataframe): reddit or twitter dataframe
        source(str): reddit or twitter
    Return:
        csv file
    '''
    # reformat the date of twitter
    if source == 'twitter':
        df['created_at'] = df['created_at'].apply(clean_time_t)

    # extract columns
    data = {'id_str': df['id_str'],
            'user.id_str': df['user.id_str'],
            'text': df['text'],
            'compound': df['compound'],
            'sentiment':df['compound'].apply(sentiment_define), # define sentiments
            'date': df['created_at'],
            'keyword': df['keyword'],
            #'misinfo': df['decision'],
            #'context': df['context'],
            'source': df['source']
            }
    df = pd.DataFrame(data)

    # Saving dataframe as a CSV file
    # filename = 'cleaned_data_'+ source + datetime.now().strftime('%Y%m%d_%H') + '.csv'
    # df.to_csv(filename) # haven't change the path to data
    # print('File saved as ', filename)

    return df