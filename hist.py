import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Se llama el .csv 
df = pd.read_csv('poblacion.csv')

df['color'] = df['u'] - df['g']


# Generacion de los graficos de interes

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Distribución principal
sns.histplot(
    data=df,
    x='color',
    hue='class',
    bins=500,
    stat='density',
    common_norm=False,
    alpha=0.5,
    edgecolor='black',
    ax=axes[0]
)

axes[0].set_xlim(-1, 3)
axes[0].set_title('Distribución principal')
axes[0].set_xlabel('Índice de color (u-g)')
axes[0].set_ylabel('Densidad')


# Valores extremos
sns.histplot(
    data=df,
    x='color',
    hue='class',
    bins=50,
    stat='count',
    common_norm=False,
    alpha=0.5,
    edgecolor='black',
    ax=axes[1]
)

axes[1].set_xlim(-13, -2)
axes[1].set_ylim(0, 3)
axes[1].set_title('Valores extremos')
axes[1].set_xlabel('Índice de color (u-g)')
axes[1].set_ylabel('Conteo')

plt.tight_layout()
plt.savefig('histograma_poblacion.png')
plt.show()


df_galaxias = df[df['class'] == 'GALAXY']
df_estrellas = df[df['class'] == 'STAR']

print(f"El promedio de indice de color de las galaxias es: {np.mean(df_galaxias['color'])}") 
print(f"El promedio de indice de color de las estrellas es: {np.mean(df_estrellas['color'])}")



