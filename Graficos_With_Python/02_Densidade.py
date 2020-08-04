# Importação das bibliotecas
import pandas as pd
import matplotlib as plt
import seaborn as sns

# Carregamento da base de dados
base = pd.read('trees.csv')
base.head

# Histograma com 10 divisões (bins) e somente para o primeiro atributo da base de dados
plt.hist(base.iloc[:,1], bins=6)

# Histograma com a linha de distribuição de frequência, com 6 disvisões (bins)
# kde - Linha de Densidade
sns.distplot(base.iloc[:,1], hist = True. kde = False,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor':'black'})

# Densidade
sns.distplot(base.iloc[:,1], hist = False. kde = True,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor':'black'})

# Densidade e Histograma
sns.distplot(base.iloc[:,1], hist = True. kde = True,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor':'black'})
