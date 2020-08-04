# Importação das bibliotecas
import pandas as pd
import matplotlib as plt
import seaborn as sns

# Carregamentos da base de dados
base = pd.read_csv('trees.csv')
base.head()

# Gráfico de dispersão considerando o volume e a dispersão
plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')

# Gráfico de linha considerando o volume e o atributo "Girth"
plt.scatter(base.Girth, base.Volume)
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')

# Gráfico de dispersão com 'afastamento' dos dados (jitter)
#fit_reg Linha de tendêcia
sns.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.3, fit_reg = False)
# x_jitter cria uma tremulação do gráfico de dispersão para não haver sobreposição dos dados nos gráfico
# fit_reg cria uma linha de tendência quando set True

