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
import pandas as pd


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
#shortest_path = calculate_shortest_path(G.copy(), source_node, target_node, weight='Weight')
#print(f"Shortest path from Node {source_node} to Node {target_node}: {shortest_path}")

# print("Function calculate_shortest_paths() ends at:", time.ctime())

# Calculate betweenness centrality
betweenness_centrality_result = calculate_betweenness_centrality(G, weight='Weight')
# Convert the dictionary to a DataFrame
betweenness_centrality_result_df = pd.DataFrame(list(betweenness_centrality_result.items()), columns=['Edge_Number', 'Betweenness_Centrality'])
betweenness_centrality_result_df.to_csv('betweenness_centrality_result.csv', index=False)
print("Function calculate_betweenness_centrality() ends at:", time.ctime())

# Calculate pagerank
pagerank_values_result = calculate_pagerank(G, weight='Weight')
# Save individual result
pagerank_values_result_df = pd.DataFrame({'Pagerank_Values': pagerank_values_result})
pagerank_values_result_df.to_csv('pagerank_values_result.csv', index=False)
print("Function calculate_pagerank() ends at:", time.ctime())

# Calculate clustering coefficient
clustering_coefficient_result = calculate_clustering_coefficient(G)
# Save individual result
clustering_coefficient_result_df = pd.DataFrame({'Clustering_Coefficient': clustering_coefficient_result})
clustering_coefficient_result_df.to_csv('clustering_coefficient_result.csv', index=False)
print("Function calculate_clustering_coefficient() ends at:", time.ctime())

# Calculate eigenvector centrality
# eigenvector_centrality_result = calculate_eigenvector_centrality(G, weight='Weight', max_iter=1000)
# Save individual result
# eigenvector_centrality_result_df = pd.DataFrame({'Eigenvector_Centrality': eigenvector_centrality_result})
# eigenvector_centrality_result_df.to_csv('eigenvector_centrality_result.csv', index=False)
# print("Function calculate_eigenvector_centrality() ends at:", time.ctime())

# Detect communities
communities_result = detect_communities(G, weight='Weight')
# Convert the dictionary to a DataFrame
communities_result_df = pd.DataFrame(list(communities_result.items()), columns=['Node', 'Community'])
communities_result_df.to_csv('communities_result.csv', index=False)
print("Function detect_communities() ends at:", time.ctime())


# Store the results in a dictionary or any other suitable data structure
results = {
    #'shortest_path_result': shortest_path_result,
    'betweenness_centrality_result': betweenness_centrality_result,
    'pagerank_values_result': pagerank_values_result,
    'clustering_coefficient_result': clustering_coefficient_result,
    # 'eigenvector_centrality_result': eigenvector_centrality_result,
    'communities_result': communities_result
}

# Save the aggregated results to a file
results_df = pd.DataFrame()

for result_name, result_data in results.items():
    if isinstance(result_data, dict):
        result_df = pd.DataFrame(list(result_data.items()), columns=['Edge_Number', result_name])
    else:
        result_df = pd.DataFrame({result_name: [result_data]})

    results_df = pd.concat([results_df, result_df], axis=1)

results_df.to_csv('results.csv', index=False)

# Visualize results
visualize_graph(G)
