import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Hello ! Importation des bibliothèques")

tabeau = np.arange(1,10).reshape(3,3)
print(tabeau)

#importation d'une base de donnée
DataFrame = pd.read_excel("s:/CERTI/SEMAINE_2/PYTHON_POUR_L_ANALYSE_DES_DONNES/python_data_analyst/jour_04/vente_magasin_analyse.xlsx")
print(DataFrame.head())