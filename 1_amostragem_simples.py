import pandas as pd
import numpy as np

#Abre o Arquivo em CSV e Faz a leitura
base = pd.read_csv(r'C:\Users\bruno\OneDrive\Python\Estatistica_WiTh_Python\Estatistica1\Dados\iris.csv')


#Travar a quantidade da amostra de 1 e 0 não variando a quantidade entre eles
np.random.seed(2345)

#Cria a amostra binária
#a = gerar 0 e 1 para a escolha da amostra
#size = tamanho da amostra
#Replace = False(Se o random sortear um número, ele não pode sorteá-lo novamente)
#P = Probabilidade de ele sortear 0 é de 50% e 1 é de 50% 
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p= [0.5,0.5])

#mostra a quantidade de 0 ou 1 que a amostra extratificou
print(len(amostra[amostra==0]))