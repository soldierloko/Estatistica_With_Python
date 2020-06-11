#Para este cálculo, deve ser atendido os seguintes critérios:
#1 Números fixos de experimentos
#2 Cada experimento pode ter 2 resultados apenas: sucesso ou fracasso
#3 A probabildade de sucesso deve ser a mesma em cada experimento
#4 Os experimentos são independentes

#Ex: Se eu jogar uma moeda 5 vezes. Qual a probabilidade de dar cara 3 vezes?
from scipy.stats import binom

prob = binom.pmf(3,5,0.5)

print(prob)

#Ex: Passar dpor 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
#0,1,2,3 ou 4 vezes seguidas

#0
print(binom.pmf(0,4,0.25))
#1
print(binom.pmf(1,4,0.25))
#2
print(binom.pmf(2,4,0.25))
#3
print(binom.pmf(3,4,0.25))
#4
print(binom.pmf(4,4,0.25))

#Probabilidade acumulativa
binom.cdf(4,4,0.25)

#Ex: Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando que cada questão tem 4 alternativas?
binom.pmf(7, 12, 0.25)