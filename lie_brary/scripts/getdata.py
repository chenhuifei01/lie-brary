from lie_brary.scripts.scrap.scrap_reddit import scrape_r
from lie_brary.scripts.scrap.scrap_twitter import scrape_t
import pandas as pd
from datetime import datetime
from lie_brary.scripts.clean.sentiment import sentiment_analysis, extract_col


topics = 'safe-t'
keywords = ['Safe-T', 'Purge Law', 'Pretrial Fairness Act']

def write_update_date():
    '''
    Concat the update date into a txt file as pandas dataframe to update_file.csv
    '''
    df = pd.read_csv('lie_brary/data/cleaned_data/update_date.csv')
    date = datetime.now().strftime("%B %d - %Y | %H:%M:%S")
    df = pd.concat([df, pd.DataFrame({'update_date': [date]})], ignore_index=True)
    df.to_csv('lie_brary/data/cleaned_data/update_date.csv', index=False)
    print('Date updated :', date)

def getdata():
    print("Update the Data")

    # read cleaned data
    df_cleaned = pd.read_csv('lie_brary/data/cleaned_data/cleaned_data.csv')
    cleaned_id_lst = list(df_cleaned['id_str'])

    # scrap data from media
    print("scrap data")
    df_r = scrape_r(keywords)
    df_t = scrape_t(keywords)


    # check and remove duplicates
    print("remove duplicates")
    dff_r = df_r[
        (~df_r.id_str.isin(cleaned_id_lst))]
    dff_t = df_t[
        (~df_t.id_str.isin(cleaned_id_lst))]

    # print("check empty")
    if dff_r.empty or dff_t.empty:
        print('No new data to update')
        write_update_date()
        return

    # sentiment analysis
    print("sentiment analysis and prediction misinfo")
    dff_r = sentiment_analysis(dff_r)
    dff_t = sentiment_analysis(dff_r)

    # clean data
    print("extract columns")
    dff_r = extract_col(dff_r)
    dff_t = extract_col(dff_t)

    df = pd.concat([df_cleaned, dff_r, dff_t], ignore_index=True)
    filename = 'cleaned_data.csv'
    df.to_csv('lie_brary/data/cleaned_data/' + filename, index=False)
    print('File updated as ', filename, 'at lie_brary/data/cleaned_data')
    write_update_date()
