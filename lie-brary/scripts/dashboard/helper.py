'''
Helper functions for dashboard
Created by: @rezapratama
'''

SENTIMENT = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']

FACT = ['NOT-FACT', 'FACT']

SOURCE = ['Twitter', 'Reddit']

KEYWORD = ['purge+law', 'safe-t', 'Pretrial Fairness Act']


def filter_data(df, sentiment, fact, source, keyword):
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
        (df.fact.isin(fact)) &
        (df.sources.isin(source)) &
        (df.keyword.isin(keyword))
    ]
    return dff

