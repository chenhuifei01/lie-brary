'''
This script is used to create the visualization function for the dashboard
Created by: @rezapratama
'''

import plotly.express as px

def barplot_fact(aggregate_df):
    '''
    Create barchart of fact
    Input:
        aggregate_df: dataframe
    Output:
        fig: barchart of fact
    '''
    fig = px.bar(aggregate_df,
            x='fact',
            y='count',
            color='sentiment',
            #color_discrete_sequence=['#00cc96', '#ff7f0e', '#d62728'],
            labels={'fact':'Fact or Non-Fact',
                    'count':'Number of Posts',
                    'sentiment':'Sentiment'},
            title='Number of Posts by Fact')
    return fig


def barplot_sentiment(aggregate_df):
    '''
    Create barchart of sentiment
    Input:
        aggregate_df: dataframe
    Output:
        fig: barchart of fact
    '''
    fig2 = px.bar(aggregate_df,
             x='sentiment',
             y='count',
             color='fact',
             labels={'fact':'Fact or Non-Fact',
                     'count':'Number of Posts',
                     'sentiment':'Sentiment'},
             title='Number of Posts by Sentiment')
    return fig2