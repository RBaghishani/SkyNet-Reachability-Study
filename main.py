from src.data_loading import load_data, create_graph
from src.graph_analysis import (
    calculate_shortest_path,
    calculate_betweenness_centrality,
    calculate_pagerank,
    calculate_clustering_coefficient,
    calculate_eigenvector_centrality,
    detect_communities
)
from src.visualization import visualize_graph
import time


# Load data
df_reachability, df_meta = load_data()

# Create graph
G = create_graph(df_reachability)

# Visualize results
# visualize_graph(G)

# Perform analysis
# Choose source and target nodes
source_node = 0
target_node = 5  # Replace with the desired target node ID

# Calculate shortest path
shortest_path = calculate_shortest_path(G.copy(), source_node, target_node, weight='Weight')
print(f"Shortest path from Node {source_node} to Node {target_node}: {shortest_path}")

print("Function calculate_shortest_paths() ends at:", time.ctime())

betweenness_centrality = calculate_betweenness_centrality(G, weight='Weight')
print("Function calculate_betweenness_centrality() ends at:", time.ctime())

pagerank_values = calculate_pagerank(G, weight='Weight')
print("Function calculate_pagerank() ends at:", time.ctime())

clustering_coefficient = calculate_clustering_coefficient(G)
print("Function calculate_clustering_coefficient() ends at:", time.ctime())

eigenvector_centrality = calculate_eigenvector_centrality(G, weight='Weight')
print("Function calculate_eigenvector_centrality() ends at:", time.ctime())

communities = detect_communities(G, weight='Weight')
print("Function detect_communities() ends at:", time.ctime())

# Store the results in a dictionary or any other suitable data structure
results = {
    'shortest_paths': shortest_paths,
    'betweenness_centrality': betweenness_centrality,
    'pagerank_values': pagerank_values,
    'clustering_coefficient': clustering_coefficient,
    'eigenvector_centrality': eigenvector_centrality,
    'communities': communities
}

# Save the results to a file or use them in further analysis
# For example, you can save to a CSV file using pandas:
# results_df = pd.DataFrame(results)
# results_df.to_csv('results.csv', index=False)

# Visualize results
visualize_graph(G)
