import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv(r"D:/python/py/pro-108.csv")
digram = pff.create_distplot([df["Avg Rating"].tolist()],["Rating"])
digram.show()