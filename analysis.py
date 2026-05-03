import pandas as pd

data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 970, 500]}

df = pd.DataFrame(data)

print("Продажі по містах (тимчасова версія):")
print(df)
# average_sales = df["sales"].mean()
