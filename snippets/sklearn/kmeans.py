# author: Maarten Breddels
# date: Wed 7 Sep 2022
# requires plotly and scikit-learn:
#  pip install plotly scikit-learn
# scikit learn documentation:
#   https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans

import plotly.express as px
import numpy as np

df = px.data.iris()


xcol, ycol = "petal_length", "sepal_length"

X = np.array(df[[xcol, ycol]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df["cluster_id"] = kmeans.predict(X)

print(kmeans.cluster_centers_)

fig1 = px.scatter(df, xcol, ycol, color="species", title="Data")
fig2 = px.scatter(df, xcol, ycol, color="cluster_id", title="Cluster ID")
display(fig1)
display(fig2)
