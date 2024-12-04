# aqui será feito o pré-processamento das palavras para a filtração apropriada.

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

dados_train = pd.read_csv('classifier-data/train.csv')
dados_test = pd.read_csv('classifier-data/test.csv') 
# dados dos arquivos csv, treino e teste

print(dados_train.head())