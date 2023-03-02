'''
Helper functions for dashboard
- R
'''
import pandas as pd

SENTIMENT = ['positive', 'negative', 'neutral']

SOURCE = ['twitter', 'reddit']


def dashboard_load_data():
    '''
    Load data for dashboard, and create new columns for filtering
    Input:
        None
    Output:
        df: dataframe
    '''
    df = pd.read_csv('lie_brary/data/cleaned_data/manual_labelled.csv')
    df['count'] = 1
    df['bydate'] = pd.to_datetime(df['date']).dt.date
    return df


def filter_data(df, sentiment, misinfo, source, keyword):
    '''
    Filter data based on user input
    Input:
        df: dataframe
        sentiment: list of sentiment
        fact: list of fact
        source: list of source
        keyword: list of keyword
        date_range: list of date range
    Output:
        dff: filtered dataframe
    '''
    dff = df[
        (df.sentiment.isin(sentiment)) &
        (df.misinfo.isin(misinfo)) &
        (df.source.isin(source)) &
        (df.keyword.isin(keyword))
    ]
    return dff

