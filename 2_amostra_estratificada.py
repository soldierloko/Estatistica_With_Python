import pandas as pd

#1 Exemplo

#Esta lib é utilizada para fazer a divisão da base de dados 
from sklearn.model_selection import train_test_split

#Abre o Arquivo em CSV e Faz a leitura
iris = pd.read_csv(r'C:\Users\bruno\OneDrive\Python\Estatistica_WiTh_Python\Estatistica1\Dados\iris.csv')

#O comando train_test_split divide a a base de dados em duas variáveis (x/y)
#-----------------------------------------------------------------------------
#A função iloc é utilizada para selecionar partes específicas da base de dados
#[:, 0:4] 
# ":" = Todas as linhas do dataframe
#[0:4] = retorna as coluna de 0 até 4 porém excluindo a 4
#O primeiro iloc deve ser mostrado o intervalo das colunas, o segundo é por qual atributo você quer fazer a divisão que neste caso foi a "class" coluna 4
#-----------------------------------------------------------------------------
#test_size = % que você vai dividir esta base de dados, no cado 50% 
#-----------------------------------------------------------------------------
#stratify = por qual atributo (coluna) iremos dividir a Base, no caso a coluna 4 usando iloc

x, _, y, _ = train_test_split(iris.iloc[:, 0:4],iris.iloc[:,4], test_size = 0.5, stratify = iris.iloc[:,4])

#-----------------------------------------------------------------------------

#2 Exemplo

#Abre o Arquivo em CSV e Faz a leitura
infert = pd.read_csv(r'C:\Users\bruno\OneDrive\Python\Estatistica_WiTh_Python\Estatistica1\Dados\infert.csv')

#Neste exemplo. estratifiquei apenas 100 registros proporcionados pela quantidade de cada atributo da 2 coluna
#Qtde de linhas do DF = 248
#Qtde de linhas a extratificar = 100
#% a ser informado no test_size = 60% para estratificar somente 100 linhas

x1, _, y1, _ = train_test_split(infert.iloc[:,2:9], infert.iloc[:,1], test_size = 0.6, stratify = infert.iloc[:,1])


