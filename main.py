from src.data_loading import load_data, create_graph
from src.graph_analysis import calculate_shortest_paths, calculate_betweenness_centrality, detect_communities
from src.visualization import visualize_graph
import time


# Load data
df_reachability, df_meta = load_data()

# Create graph
G = create_graph(df_reachability)

# Visualize results
# visualize_graph(G)

# Perform analysis
shortest_paths = calculate_shortest_paths(G, 'NodeA', 'Weight')
print("Function calculate_shortest_paths() ends at:", time.ctime())

betweenness_centrality = calculate_betweenness_centrality(G, 'Weight')
print("Function calculate_betweenness_centrality() ends at:", time.ctime())

communities = detect_communities(G, 'Weight')
print("Function detect_communities() ends at:", time.ctime())


# Visualize results
visualize_graph(G)
