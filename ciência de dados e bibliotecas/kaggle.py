import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/kaggle/input/viral-social-media-trends-and-engagement-analysis/Viral_Social_Media_Trends.csv')
# dff = pd.read_csv ('/kaggle/input/world-population-dataset/world_population.csv')



# dff1 = dff.loc[0:7,['Year']]


# print (df.columns)

# print (df.head())
# print (dff.head())

# comparação 1 ================================


a = (4163464,4155940,3666211,917951,64866)
explode = (0.1,0,0,0,0)
labels = ['Uk','India','Brazil','Australia','Brazil']
plt.pie(a,explode = explode, labels=labels,autopct='%.2f%%',shadow=True)
plt.title('Visualizações  (total= 1.180.300)')



# comparação 2 ================================



plataforma = ['TikTok(UK)', 'Instagram', 'Twitter', 'YouTube', 'TikTok(Brazil)']
views = [4163464, 4155940, 3666211, 917951, 64866]
plt.figure(figsize=(10,6))
plt.xlabel('Plataforma')
plt.ylabel('Visualizações')
bars = plt.bar(plataforma, views)


plt.bar_label(bars, labels=[f'{v:,.0f}' for v in views], padding=5)

plt.show()


# comparação 3 ================================





pais = ('UK(TikTok)', 'India(Instagram)', 'Brazil(Twitter)', 'Australia(Youtube)', 'Brazil(TikTok)')

likes = (339431,215240,327143,127125,171361)
plt.figure(figsize=(20,10))

bars = plt.barh(pais, likes, color='green') 

plt.bar_label(bars, labels=[f'{v:,.0f}' for v in likes], padding=3)
plt.ylabel("Países")
plt.xlabel("Likes")
plt.title("Psíses com mais likes")
plt.show()



# comparação 4 ================================







# plt.plot((2016, 2017, 2018, 2019, 2020), (206163053, 207833823, 209469323, 211049527, 212559417), 'mv-.', label='Linha 1')


# plt.grid(True)


# plt.xlabel('Ano')
# plt.ylabel('População')
# plt.title('TABELA')


# plt.legend()

# plt.show()