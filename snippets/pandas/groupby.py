import pandas
import plotly

df = plotly.data.iris()

dfg = df.groupby(["species"]).agg(petal_width_mean=("petal_width", "mean"), sepal_width_mean=("sepal_width", "mean")).reset_index()
print(dfg)