import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Lecture des données
df = pd.read_csv('financial_data.csv', parse_dates=['Date'])

# Agrégation mensuelle pour une meilleure lisibilité
df_monthly = df.resample('M', on='Date').sum().reset_index()

# Calcul des seuils critiques
# Par exemple :
# - Revenu mensuel minimum souhaité : 3 000 000
# - Dépenses mensuelles maximum acceptable : 2 100 000
revenue_threshold = 3000000
expenses_threshold = 2100000

# Création du graphique
plt.figure(figsize=(14, 8))

# Tracé du Revenu
plt.plot(df_monthly['Date'], df_monthly['Revenu'], label='Revenu', color='green')
# Remplissage en fonction du seuil
plt.fill_between(df_monthly['Date'], df_monthly['Revenu'], revenue_threshold,
                 where=df_monthly['Revenu'] < revenue_threshold,
                 facecolor='red', alpha=0.3, label='Revenu en dessous du seuil')

# Tracé des Dépenses
plt.plot(df_monthly['Date'], df_monthly['Dépenses'], label='Dépenses', color='blue')
# Remplissage en fonction du seuil
plt.fill_between(df_monthly['Date'], df_monthly['Dépenses'], expenses_threshold,
                 where=df_monthly['Dépenses'] > expenses_threshold,
                 facecolor='orange', alpha=0.3, label='Dépenses au-dessus du seuil')

# Tracé du Profit
plt.plot(df_monthly['Date'], df_monthly['Profit'], label='Profit', color='purple')

# Ajout des seuils
plt.axhline(revenue_threshold, color='red', linestyle='--', linewidth=1)
plt.axhline(expenses_threshold, color='orange', linestyle='--', linewidth=1)

# Mise en forme
plt.title('Données Financières Mensuelles (2015-2024)')
plt.xlabel('Date')
plt.ylabel('Montant (en USD)')
plt.legend()
plt.grid(True)

# Format de l'axe des x
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
