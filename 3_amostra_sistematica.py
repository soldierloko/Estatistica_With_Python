import numpy as np
import pandas as pd

#A função Ceil faz o arredondamento
from math import ceil

#Tamanho da população a ser sorteada
populacao = 150
#Qtde da amostra
amostra = 14
#Arredondamento da amostra
k = ceil(populacao / amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k

base = pd.read_csv(r'C:\Users\bruno\OneDrive\Python\Estatistica_WiTh_Python\Estatistica1\Dados\iris.csv')

base_final = base.loc[sorteados]


#Esse tipo de amostra serve para pegar amostra de acordo com regras definidas (A cada 10 registros, pegue o próximo)