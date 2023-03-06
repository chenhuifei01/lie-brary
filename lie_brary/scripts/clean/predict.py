'''
This file is used to predict whether a post is misinfo or not.
Author: Xiomara Salazar
Debugged by Reza R Pratama
'''

import pickle

def predict(text):
    """
    Takes in a post or tweet and return prediction of whether it is misinfo (1)
    or not (0)

    Input:
        Post - string of text from pos that you want to classify

    Return:
        Decision - 0 if it is not misinfo and 1 if it is misinfo
    """
    clf = pickle.load(open("lie_brary/scripts/clean/model.pkl", "rb"))
    vec = pickle.load(open("lie_brary/scripts/clean/count_vect.pkl", "rb"))
    text_tfidf = vec.transform([text])
    y_pred = clf.predict(text_tfidf)

    if y_pred[0] == 1:
        return "misinformation"
    else:
        return "not-misinfo"