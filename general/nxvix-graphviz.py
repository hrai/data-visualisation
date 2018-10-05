import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# import pygraphviz_layout
 
# Build a dataframe with your connections
df = pd.read_csv('data.csv')
df
 
# Build your graph
# G=nx.from_pandas_edgelist(df, 'from', 'to', ['weight'])
G = nx.read_edgelist('data-weight.csv', data=(('weight', int),), create_using=nx.DiGraph(), delimiter=',', nodetype=int, encoding="utf-8")
print(G.edges(data=True))
 
# # Fruchterman Reingold
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.fruchterman_reingold_layout(G))
# plt.title("fruchterman_reingold")
 
# # Circular
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.circular_layout(G))
# plt.title("circular")
 
# # Random
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.random_layout(G))
# plt.title("random")
 
# # Spectral
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.spectral_layout(G))
# plt.title("spectral")
 
# Spring
nx.draw(
G,
with_labels=True,
node_size=1000,
node_color="skyblue",
arrows=True,
arrowsize=15,
# pos=nx.spring_layout(G, k=0.15, iterations=20))
pos=nx.nx_agraph.graphviz_layout(G, prog='dot', args='-Goverlap=false'))
# pos=nx.spring_layout(G))

plt.title("spring")

plt.show()
