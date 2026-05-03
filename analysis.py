import pandas as pd

data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 95git add analysis.py0, 500]}

df = pd.DataFrame(data)

print("Продажі по містах (тимчасова версія):")
print(df)
print("Середнє значення:", df["sales"].mean())
