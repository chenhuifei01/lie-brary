from lie_brary.scripts.scrap.scrap_reddit import scrape_r
from lie_brary.scripts.scrap.scrap_twitter import scrape_t
import pandas as pd
# from clean.classifier import
from lie_brary.scripts.clean.sentiment import sentiment_analysis, extract_col

topics = 'safe-t'
keywords = ['Safe-T', 'Purge Law', 'Pretrial Fairness Act']

def getdata():
    print("Update the Data")

    # # run for the first cleaned data
    # # scrap data from media
    # df_r = scrape_r(keywords)
    # df_t = scrape_t(keywords)

    # # # train misinfo
    # # df_r = trained(df_r)
    # # df_t = trained(df_r)

    # # sentiment analysis
    # df_r = sentiment_analysis(df_r)
    # df_t = sentiment_analysis(df_r)

    # # clean data
    # df_r = extract_col(df_r, 'reddit')
    # df_t = extract_col(df_t, 'twitter')

    # # combine two dataframes from different sources and generate combined csv
    # df = df_r.append(df_t)
    # filename = 'cleaned_data.csv'
    # df.to_csv('lie_brary/data/cleaned_data/' + filename)
    # print('File saved as ', filename, 'at lie_brary/data/cleaned_data')

    # Aftere the first run, run for update cleaned data
    # read the original cleaned data
    df_cleaned = pd.read_csv('lie_brary/data/cleaned_data/cleaned_data.csv')
    cleaned_id_lst = list(df_cleaned['id_str'])

    # scrap data from media
    df_r = scrape_r(keywords)
    df_t = scrape_t(keywords)

    # check and remove duplicates
    dff_r = df_r[
        (~df_r.id_str.isin(cleaned_id_lst))]
    dff_t = df_t[
        (~df_t.id_str.isin(cleaned_id_lst))]

    # test misinfo
    #dff_r = trained(dff_r)
    #dff_t = trained(dff_r)

    # sentiment analysis
    dff_r = sentiment_analysis(dff_r)
    dff_t = sentiment_analysis(dff_r)

    # clean data
    dff_r = extract_col(dff_r, 'reddit')
    dff_t = extract_col(dff_t, 'twitter')

    # combine two dataframes from different sources and generate combined csv
    df = df_cleaned.append(dff_r, ignore_index=True)
    df = df_cleaned.append(dff_t, ignore_index=True)
    filename = 'cleaned_data.csv'
    df.to_csv('lie_brary/data/cleaned_data/' + filename, index=False)
    print('File updated as ', filename, 'at lie_brary/data/cleaned_data')
