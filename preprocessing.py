# aqui será feito o pré-processamento das palavras para a filtração apropriada.

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

data = pd.read_csv('data/ag_news.csv')  # Atualize o caminho conforme necessário
print(data.head())
