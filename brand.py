import pandas as pd 
import plotly.figure_factory as ff 
df = pd.read_csv("PRO-C108-main/data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Ratings"])
fig.show()