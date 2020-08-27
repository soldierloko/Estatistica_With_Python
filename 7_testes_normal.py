#Testando para ver se a amostra tem uma distribuição normal
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


#A Função RVS serve para gerarmos dados para a distribuição normal
dados = norm.rvs(size = 100)

stats.probplot(dados, plot = plt)

#Teste de Shapiro para saber se é umas distribuioção nomal...se maior que 0,5 = norma
stats.shapiro(dados)