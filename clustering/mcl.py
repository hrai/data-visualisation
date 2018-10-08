import markov_clustering as mc
import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt

# number of nodes to use
numnodes = 45

with open('data.csv','rb') as f:
    G = nx.read_edgelist(f,delimiter=',')

# then get the adjacency matrix (in sparse form)
matrix = nx.to_scipy_sparse_matrix(G)

result = mc.run_mcl(matrix, inflation=4)
# result = mc.run_mcl(matrix)
clusters = mc.get_clusters(result)

mc.draw_graph(matrix, clusters, node_size=50, with_labels=False, edge_color="silver")

plt.title("Un-weighted Markov Clustering Algorithm")

plt.show()
