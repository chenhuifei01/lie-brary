from lie_brary.scripts.clean.training import create_classifier
import pickle

def predict(x):
    """
    Takes in a post or tweet and return prediction of whether it is misinfo (1)
    or not (0)

    Input:
        Post - string of text from pos that you want to classify

    Return:
        Decision - 0 if it is not misinfo and 1 if it is misinfo
    """
    clf, count_vect = create_classifier()
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    sample = count_vect.transform([x])

    result = pickled_model.predict(sample)

    return result