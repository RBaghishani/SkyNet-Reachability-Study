import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()
