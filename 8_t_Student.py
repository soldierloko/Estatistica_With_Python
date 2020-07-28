from scipy.stats import t

#Média de salário dos cientistas de dados = R$ 75,00 por hora
#Amostra com 9 funcionários e desvio padrão = 10

#Qual a probabilidade de selecionar um cientista de dados e o salário
#Ser menor que R$ 80 por hora

#Lado esquerdo da Distribuição
t.cdf(1.5,8)

#Qual a probabilidade do slário ser maior que R$ 80,00

#Lado direito da distribuição
t.sf(1.5,8)

#Somando os 2, o valor deve ser igual a 1