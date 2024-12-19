import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Paramètres de génération
start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 12, 31)
delta = timedelta(days=1)

dates = []
revenues = []
expenses = []
profits = []

current_date = start_date
np.random.seed(0)  # Pour la reproductibilité

while current_date <= end_date:
    dates.append(current_date.strftime('%Y-%m-%d'))
    
    # Génération de revenus entre 50k et 150k avec une tendance annuelle
    year_fraction = (current_date - start_date).days / 365.25
    revenue = 100000 + 5000 * year_fraction + np.random.normal(0, 10000)
    revenues.append(max(revenue, 50000))  # Revenus minimum de 50k
    
    # Génération des dépenses entre 30k et 120k avec une tendance
    expense = 70000 + 3000 * year_fraction + np.random.normal(0, 8000)
    expenses.append(max(expense, 30000))  # Dépenses minimum de 30k
    
    # Calcul du profit
    profit = revenue - expense
    profits.append(profit)
    
    current_date += delta

# Création du DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Revenu': revenues,
    'Dépenses': expenses,
    'Profit': profits
})

# Sauvegarde en CSV
df.to_csv('financial_data.csv', index=False)

print("Le fichier 'financial_data.csv' a été généré avec succès.")
