import networkx as nx
from community import community_louvain

def calculate_shortest_path(graph, source_node, target_node, weight):
    remove_negative_cycles(graph)
    return nx.johnson(graph, weight=weight)[source_node][target_node]

def calculate_betweenness_centrality(graph, weight):
    return nx.betweenness_centrality(graph, weight=weight)

def calculate_pagerank(graph, weight):
    return nx.pagerank(graph, weight=weight)

def calculate_clustering_coefficient(graph):
    return nx.clustering(graph)

def calculate_eigenvector_centrality(graph, weight):
    return nx.eigenvector_centrality(graph, weight=weight)

def detect_communities(graph, weight):
    return community_louvain.best_partition(graph, weight=weight)

# Add additional network metric calculations
def calculate_degree_centrality(graph):
    return nx.degree_centrality(graph)

def calculate_closeness_centrality(graph, weight):
    return nx.closeness_centrality(graph, distance=weight)

def calculate_average_neighbor_degree(graph):
    return nx.average_neighbor_degree(graph)

def remove_negative_cycles(graph):
    # Detect and remove negative cycles
    negative_cycles = list(nx.simple_cycles(graph))
    for cycle in negative_cycles:
        for i in range(len(cycle) - 1):
            graph.remove_edge(cycle[i], cycle[i+1])
        graph.remove_edge(cycle[-1], cycle[0])