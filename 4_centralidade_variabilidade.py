import numpy as np
from scipy import stats

#Valores de salário dos jogadores
jogadores = [40000,18000,12000,25000,30000,140000,30000,40000,800000]

#Calcula a média dos salários
print(np.mean(jogadores))

#Calcula a mediana dos salários
print(np.median(jogadores))

#Calcula a quartis dos salários
print(np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1]))

#Calcula a desvio padrão dos salários
print(np.std(jogadores, ddof=1))

#Calcula tudo de uma vez
print(stats.describe(jogadores))


