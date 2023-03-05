import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer


def preprocess_training_data():
    """
    Imports csv file with labeled data (0 for not misinfo, 1 for misinfo) and
    creates:
    - features, 
    - tfidf: a statistical measure that evaluates how relevant 
    a word is to a document in a collection of documents
    - labels
    - df: a dataframe of labeled posts/tweets


    Return tfdi, features, labels (0,1 labels)
    """
    #we labeled 606 pieces of content to create classifier
    filename = 'lie_brary/data/cleaned_data/manual_labeld_all.csv'

    df = pd.read_csv(filename)
    df.dropna(inplace=True)
    df.head()

    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', \
        encoding='latin-1', ngram_range=(1, 2), stop_words='english')
    features = tfidf.fit_transform(df.text).toarray()
    labels = df.misinfo

    return tfidf, features, labels, df 



def build_grams(tfidf, features, labels):
    """
    Find the terms that are most correlated with misinfo/not misinfo categories

    Input:
    - tfidf
    - features
    - labels

    Prints unigrams and bigrams that are correlated with labels (misinfo, not
    misinfo)
    """
    category_to_id = {'Misinfo': 1, 'Not misinfo': 0}
    N = 2
    for classification, class_id in sorted(category_to_id.items()):
        features_chi2 = chi2(features, labels == class_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names_out())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
        print("# '{}':".format(classification))
        print("  . Most correlated unigrams:\n. {}".format('\n. '.join(\
            unigrams[-N:])))
        print("  . Most correlated bigrams:\n. {}".format('\n. '.join(\
            bigrams[-N:])))


def create_classifier():
    """
    Creates classifier to assess whether a text is misinfo or not

    Input: 
    - df: dataframe of label data

    Returns:
        clf - the classifier
        count_vect - Convert texts into a matrix of token counts


    """
    tfidf, features, labels, df = preprocess_training_data()
    X_train, X_test, y_train, y_test = train_test_split(df['text'], \
        df['misinfo'], random_state = 0)

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    clf = MultinomialNB().fit(X_train_tfidf, y_train)

    pickle.dump(clf, open('model.pkl', 'wb'))

    return clf, count_vect

# def predict_clf():
#     """
#     Takes a str and predicts classification based on training data

#     Input:
#     - new str to classify
#     - classifier
#     """
#     filename = 'test_manual_labeld_twitter.csv'
#     tfidf, features, labels, df  = preprocess_data(filename)

#     build_grams(tfidf, features, labels)

#     clf, count_vect = create_classifier(df)

#     #print(clf.predict(count_vect.transform([str])))
#     return clf, count_vect

    