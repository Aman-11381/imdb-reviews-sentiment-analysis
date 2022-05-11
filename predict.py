import pandas as pd
import numpy as np
import pickle

async def get_sentiment(review):
    review_list = np.array([review])
    test_review = pd.Series(review_list)

    cv = pickle.load(open('static/pickle/cv.pkl', 'rb'))
    lr = pickle.load(open('static/pickle/lr.pkl', 'rb'))
    le = pickle.load(open('static/pickle/le.pkl', 'rb'))

    result_encoded = lr.predict(cv.transform(test_review))
    result = le.inverse_transform(result_encoded)

    return result
    
