import pandas as pd

df = pd.read_excel("Reference_aircraft.xlsx", sheet_name="Sheet 1")

print(df.head())
