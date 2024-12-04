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

stop_words = set(stopwords.words('english'))
# como as notícias estão em inglês, a variável é configurada para identificar stopwords nesse idioma.
# essas palavras são irrelevantes pra indexação e classificação do conteúdo nesse contexto.

stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [stemmer.stem(w) for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(filtered_tokens)

dados_train['processed_text'] =dados_train['text_column'].apply(preprocess_text)  # Substitua 'text_column' pela coluna correta
