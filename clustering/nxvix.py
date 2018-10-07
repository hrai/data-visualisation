# import pandas as pd
import matplotlib.pyplot as plt
# import pygraphviz_layout
import markov_clustering as mc
import networkx as nx
import random

# number of nodes to use
numnodes = 200

# generate random positions as a dictionary where the key is the node id and the value
# is a tuple containing 2D coordinates
positions = {i:(random.random() * 2 - 1, random.random() * 2 - 1) for i in range(numnodes)}

# use networkx to generate the graph
network = nx.random_geometric_graph(numnodes, 0.3, pos=positions)

# then get the adjacency matrix (in sparse form)
matrix = nx.to_scipy_sparse_matrix(network)
result = mc.run_mcl(matrix)           # run MCL with default parameters
clusters = mc.get_clusters(result)    # get clusters

mc.draw_graph(matrix, clusters, pos=positions, node_size=50, with_labels=False, edge_color="silver")



# # Build a dataframe with your connections
# df = pd.read_csv('data-weight.csv')
# df
 
# # Build your graph
# G=nx.from_pandas_edgelist(df, 'from', 'to', ['weight'])
# print(G.edges(data=True))

# # Spring
# nx.draw(
# G,
# with_labels=True,
# node_size=1000,
# node_color="skyblue",
# arrows=True,
# arrowsize=15,
# # pos=nx.spring_layout(G, k=15, iterations=20))
# pos=nx.spring_layout(G))

# plt.title("spring")

# plt.show()
