import pandas as pd
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from datetime import datetime


sia = SentimentIntensityAnalyzer()
# example
# sia.polarity_scores('I am so happy!')
# Output: {'neg': 0.0, 'neu': 0.318, 'pos': 0.682, 'compound': 0.6468}

def sentiment_analysis(df):
    # Run the polarity score on the entire dataset
    res = {}
    for i, row in tqdm(df.iterrows(), total = len(df)):
        text = row['text']
        myid = row['id_str']
        res[myid] = sia.polarity_scores(text)
    vaders = pd.DataFrame(res).T
    vaders = vaders.reset_index().rename(columns = {'index':'id_str'})
    vaders = vaders.merge(df, how = 'left')
    #     break
    return vaders


def sentiment_define(x):
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
    data = {'id_str': df['id_str'],
            'user.id_str': df['user.id_str'],
            'text': df['text'],
            'compund': df['compound'],
            'sentiment':df['compound'].apply(sentiment_define),
            'date': df['created_at'], 
            'keyword': df['keyword'],
            'misinfo': df['decision'],
            'context': df['context'],
            'source': source}
    df = pd.DataFrame(data)
    return df