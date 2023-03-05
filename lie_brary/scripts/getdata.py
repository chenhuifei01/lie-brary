from lie_brary.scripts.scrap.scrap_reddit import scrape_r
from lie_brary.scripts.scrap.scrap_twitter import scrape_t
import pandas as pd
# from clean.classifier import
from lie_brary.scripts.clean.sentiment import sentiment_analysis, extract_col


topics = 'safe-t'
keywords = ['Safe-T', 'Purge Law', 'Pretrial Fairness Act']


# def check_empty(df1, df2):
#     # df = pd.Dataframe()
#     if df1.empty and df2.empty:

#     return df

# df = check_empty(df_r, df_t)

def getdata():
    print("Update the Data")

    # read cleaned data
    df_cleaned = pd.read_csv('lie_brary/data/cleaned_data/cleaned_data.csv')
    cleaned_id_lst = list(df_cleaned['id_str'])

    # # scrap data from media
    # df_r = scrape_r(keywords)
    # df_t = scrape_t(keywords)

    # # extract column
    # df_r = df_r[['id_str', 'user.id_str', 'text', 'created_at', 'keyword', 'source']]
    # df_t = df_t[['id_str', 'user.id_str', 'text', 'created_at', 'keyword', 'source']]
    
    # # # df_r.reset_index(drop=True, inplace=True)
    # # # df_t.reset_index(drop=True, inplace=True)

    # # df = pd.concat( [df_r, df_t], ignore_index = True) 
    # # concate dataframe
    # # df = pd.concat([df_r, df_t], ignore_index = True)
    # # df = df_r.append(df_t) 

    # # check and remove duplicates
    # dff_r = df_r[
    #     (~df_r.id_str.isin(cleaned_id_lst))]
    # dff_t = df_t[
    #     (~df_t.id_str.isin(cleaned_id_lst))]



    # # dff = pd.concat([dff_r, dff_t])
    # dff = pd.DataFrame()

    # # check empty dataframe
    # if dff_r.empty:
    #     print('No new reddit data to update')
    # else:
    #     # dff.append(dff_r)
    #     dff = pd.concat([dff, dff_r], ignore_index=True)
    # if dff_t.empty:
    #     print('No new twitter data to update')
    # else:
    #     # dff.append(dff_t)
    #     dff = pd.concat([dff, dff_t], ignore_index=True)
    # if dff.empty:
    #     return
    

    # # test misinfo
    # # dff_r = trained(dff_r)
    # # dff_t = trained(dff_r)

    # # sentiment analysis
    # dff = sentiment_analysis(dff)

    # # clean data
    # dff = extract_col(dff)

    # df = pd.concat([df_cleaned, dff], ignore_index = True)
    # filename = 'cleaned_data.csv'
    # df.to_csv('lie_brary/data/cleaned_data/' + filename, index=False)
    # print('File updated as ', filename, 'at lie_brary/data/cleaned_data')




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
