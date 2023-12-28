import networkx as nx
from community import best_partition

def calculate_shortest_paths(graph, source, weight):
    return nx.single_source_dijkstra_path_length(graph, source=source, weight=weight)

def calculate_betweenness_centrality(graph, weight):
    return nx.betweenness_centrality(graph, weight=weight)

def detect_communities(graph, weight):
    return best_partition(graph, weight=weight)
