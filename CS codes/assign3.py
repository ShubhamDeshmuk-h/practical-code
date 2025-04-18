import nltk
 from nltk.corpus import stopwords
 import string
 import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns
 from sklearn.model_selection import train_test_split
 from sklearn.pipeline import Pipeline
 from sklearn.feature_extraction.text import CountVectorizer, 
TfidfTransformer
 from sklearn.naive_bayes import MultinomialNB
 from sklearn.metrics import classification_report, confusion_matrix
 # Load dataset
 messages = pd.read_csv('spam.csv', encoding='latin-1')
 messages.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, 
inplace=True)
 messages = messages.rename(columns={'v1': 'class', 'v2': 'text'})
 # Add message length feature
 messages['length'] = messages['text'].apply(len)
 # Plot message length distribution
 messages.hist(column='length', by='class', bins=50, figsize=(15, 6))
 plt.show()