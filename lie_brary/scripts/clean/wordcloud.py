import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

stopwords = STOPWORDS
safe_T = ['SAFE', 'T', 'Act','https','co','s']
stopwords.update(safe_T)

#Generating a word cloud from text of content labeled as misinformation
def word_cloud(df):
    wc = WordCloud(
        background_color = 'white',
        stopwords = stopwords,
        height = 600,
        width = 800)
    
    misstr = ''
    for title in df[df['misinfo'] == 1]['text']:
        misstr += title   

    wc.generate(misstr)
    plt.imshow(wc)
    plt.axis('off')
    wc.to_file('wordcloud.png')
    plt.show()


#Generating a word cloud for text based on its associated sentiment -
#positive, negative or neutral

def word_cloud_sent(df):
    wc = WordCloud(
        background_color = 'white',
        stopwords = stopwords,
        height = 600,
        width = 800)
    
    neg_str = ''
    for title in df[df['compound'] <0]['text']:
        neg_str += title
    wc.generate(neg_str)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('wordcloud_neg.png')
    
    pos_str =''
    for title in df[df['compound'] > 0 ]['text']:
        pos_str += title
    wc.generate(pos_str)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('wordcloud_pos.png')
    
    neu_str = ''
    for title in df[df['compound'] == 0]['text']:
        neu_str += title    
    wc.generate(neu_str)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('wordcloud_neu.png')
