
import networkx as nx
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import matplotlib.patches as mpatches


def path_exists(G, node1, node2):
    #This function checks whether a path exists between two nodes (node1, node2) in graph G.
    visited_nodes = set()
    queue = [node1]
    for node in queue:
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break
        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])
             # Check to see if the final element of the queue has been reached
        if node == queue[-1]:
            print('Path does not exist between nodes {0} and {1}'.format(node1, node2))
            return False


def example():
    return 5


# TO NORMALIZE
def normalize(df_columns):
    x=df_columns.values.astype(float)
    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler()
    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(x)
    # Run the normalizer on the dataframe
    return x_scaled


# Scatter plotting

def my_scatter(x,y, title, trend=True):
    plt.scatter(x, y)
    if trend:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), "r--")
    plt.title(title)
    plt.show()