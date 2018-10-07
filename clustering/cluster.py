import markov_clustering as mc
import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt

# number of nodes to use
numnodes = 0

df = pd.read_csv('data.csv')

# generate random positions as a dictionary where the key is the node id and the value
# is a tuple containing 2D coordinates
# positions = {i:(random.random() * 2 - 1, random.random() * 2 - 1) for i in range(numnodes)}

# for i in positions:
#     print(i)
#     print(positions[i])

positions= {}
with open('data.csv') as f:
    for index, line in enumerate(f):
        (key, val) = line.split(",")
        positions[index] = (int(key), int(val))
        numnodes = index

# for i in positions:
#     print(i)
#     print(positions[i])

print(numnodes)
# use networkx to generate the graph
network = nx.random_geometric_graph(numnodes, 0.3, pos=positions)

# then get the adjacency matrix (in sparse form)
matrix = nx.to_scipy_sparse_matrix(network)

# result = mc.run_mcl(matrix, inflation=1.4)
result = mc.run_mcl(matrix)
clusters = mc.get_clusters(result)
mc.draw_graph(matrix, clusters, pos=positions, node_size=50, with_labels=False, edge_color="silver")

plt.show()
