
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

def train_model():
    df = pd.read_csv('food_dataset.csv')
    X = df[['salt_content', 'user_rating']]
    y = df['taste_intensity']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

def predict_taste(salt, rating):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([[salt, rating]])[0]
