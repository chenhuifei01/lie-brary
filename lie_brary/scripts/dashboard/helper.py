'''
Helper functions for dashboard
- R
'''
import pandas as pd

SENTIMENT = ['positive', 'negative', 'neutral']
SOURCE = ['twitter', 'reddit']
FACT = ['misinformation','not-misinfo']
KEYWORD = ['Pretrial Fairness Act','Safe-T','Purge Law','purge+law']

# Create Control List
sentiment_options = [{'label': label, 'value': label} for label in SENTIMENT]
fact_options = [{'label': label, 'value': label} for label in FACT]
source_options = [{'label': label, 'value': label} for label in SOURCE]
keyword_options = [{'label': label, 'value': label} for label in KEYWORD]


def dashboard_load_data():
    '''
    Load data for dashboard, and create new columns for filtering
    Input:
        None
    Output:
        df: dataframe
    '''
    df = pd.read_csv('lie_brary/data/cleaned_data/cleaned_data.csv')
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

def get_last_update():
    '''
    Get the last update date
    Output:
        last_update: string
    '''
    df = pd.read_csv('lie_brary/data/cleaned_data/update_date.csv')
    last_update = df['update_date'].iloc[-1]
    return "last updated: "+ str(last_update)


def datatable_load_data():
    '''
    Load data for datatable
    Input:
        None
    Output:
        df: dataframe
    '''
    df = pd.read_csv('lie_brary/data/cleaned_data/cleaned_data.csv')
    df = df[['id_str','date','text','sentiment', 'misinfo', 'source']]
    return df