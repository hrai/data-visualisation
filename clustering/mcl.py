import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# import pygraphviz_layout
 
# Build a dataframe with your connections
df = pd.read_csv('data-weight.csv')
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to', ['weight'])
print(G.edges(data=True))
 
# Spring
nx.draw(
G,
with_labels=True,
node_size=1000,
node_color="skyblue",
arrows=True,
arrowsize=15,
# pos=nx.spring_layout(G, k=15, iterations=20))
pos=nx.spring_layout(G))

plt.title("spring")

plt.show()