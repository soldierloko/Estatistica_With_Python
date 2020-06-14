#Validar se os dados estão distribuidos normalmente: Melhor forma para se fazer isso é gerar um histograma dos dados (Gráfico de Barras), onde é observado o formato de sino com a média ao centro

from scipy.stats import norm


#Conjunto de objetos em uma cesta, a média é 9 e o desvio padrão é 2
#Qual a Probabilidade de tirar um objeto com peso menor que 6 quilos?
norm.cdf(6, 8, 2)

#Qual a Probabilidade de tirar um objeto com peso maior que 6 quilos?
norm.sf(6, 8, 2)
#or
1-norm.cdf(6, 8, 2)

#Qual a probabilidade de tirar um objeto que o peso é menor que 6 ou maior que 10 quilos?
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

#Qual a probabilidade de tirar um objeto que o peso é menor que 10 e maior que 8 quilos?
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)

#Critérios da função
#1 - Quilos
#2 - Média
#3 - Desvio Padrão