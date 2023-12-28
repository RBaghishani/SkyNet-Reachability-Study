from src.data_loading import load_data, create_graph
from src.graph_analysis import calculate_shortest_paths, calculate_betweenness_centrality, detect_communities
from src.visualization import visualize_graph

# Load data
df_reachability, df_meta = load_data()

# Create graph
G = create_graph(df_reachability)

# Perform analysis
shortest_paths = calculate_shortest_paths(G, 'NodeA', 'Weight')
betweenness_centrality = calculate_betweenness_centrality(G, 'Weight')
communities = detect_communities(G, 'Weight')

# Visualize results
visualize_graph(G)
