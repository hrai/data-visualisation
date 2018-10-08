
import markov_clustering as mc
import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt

# number of nodes to use
numnodes = 0


positions= {}
(from_node, to_node, weight) = "0,1,1".split(",")
positions[0] = (int(from_node), int(to_node), int(weight))

for i in positions:
    print(i)
    print(positions[i])

