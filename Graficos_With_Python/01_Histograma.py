#Importação das Bibliotecas
import pandas as pd
import numpy as np
import marplotilib.pyplot as plt

#Carregamento da base de Dados
base = pd.read('trees.csv')
base.shape

#Dados
base.head()

#Criação do histograma, considerando somente o segundo atributo da base de dados e com duas divisões (bins)
#A variável 'h' armazena as faixas de valores Height
h = np.histogram(base.iloc[:,1], bins = 6)

#Visualização do histogramas com 6 divisões (bins)
plt.hist(base.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')