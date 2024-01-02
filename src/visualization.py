import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def visualize_graph(graph):
    # Remove or replace nan values in the edge data
    graph_with_no_nans = graph.copy()
    graph_with_no_nans.remove_edges_from([(u, v) for u, v, wt in graph.edges(data=True) if pd.isnull(wt)])

    # Draw the graph
    nx.draw(graph_with_no_nans, with_labels=True, font_weight='bold')
    plt.show()