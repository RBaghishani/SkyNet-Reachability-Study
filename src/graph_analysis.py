import networkx as nx
from community import community_louvain
import pandas as pd
import time

def calculate_betweenness_centrality(graph, weight):
    return nx.betweenness_centrality(graph, weight=weight)

def calculate_pagerank(graph, weight):
    return nx.pagerank(graph, weight=weight)

def calculate_clustering_coefficient(graph):
    return nx.clustering(graph)

# Add additional network metric calculations
def calculate_degree_centrality(graph):
    return nx.degree_centrality(graph)

# def calculate_closeness_centrality(graph, weight):
#     return nx.closeness_centrality(graph, distance=weight)

def calculate_average_neighbor_degree(graph):
    return nx.average_neighbor_degree(graph)


def calculations(G, metric):
    # Calculate degree centrality
    degree_centrality_result = calculate_degree_centrality(G)
    degree_centrality_result_df = pd.DataFrame(list(degree_centrality_result.items()), columns=['Edge_Number', 'Degree_Centrality'])
    degree_centrality_result_df.to_csv('./output/' + metric + '/degree_centrality_result_' + metric + '.csv', index=False)
    print("Function calculate_degree_centrality() ends at:", time.ctime())

    # Calculate average neighbor degree
    average_neighbor_degree_result = calculate_average_neighbor_degree(G)
    average_neighbor_degree_result_df = pd.DataFrame(list(average_neighbor_degree_result.items()), columns=['Edge_Number', 'Average_Neighbor_Degree'])
    average_neighbor_degree_result_df.to_csv('./output/' + metric + '/average_neighbor_degree_result_' + metric + '.csv', index=False)
    print("Function calculate_average_neighbor_degree() ends at:", time.ctime())

    # Calculate betweenness centrality
    betweenness_centrality_result = calculate_betweenness_centrality(G, weight='Weight')
    # Convert the dictionary to a DataFrame
    betweenness_centrality_result_df = pd.DataFrame(list(betweenness_centrality_result.items()), columns=['Edge_Number', 'Betweenness_Centrality'])
    betweenness_centrality_result_df.to_csv('./output/' + metric + '/betweenness_centrality_result_' + metric + '.csv', index=False)
    print("Function calculate_betweenness_centrality() ends at:", time.ctime())

    # Calculate pagerank
    pagerank_values_result = calculate_pagerank(G, weight='Weight')
    # Save individual result
    pagerank_values_result_df = pd.DataFrame(list(pagerank_values_result.items()),columns=['Edge_Number', 'Pagerank_Values'])
    pagerank_values_result_df.to_csv('./output/' + metric + '/pagerank_values_result_' + metric + '.csv', index=False)
    print("Function calculate_pagerank() ends at:", time.ctime())

    # Calculate clustering coefficient
    clustering_coefficient_result = calculate_clustering_coefficient(G)
    # Save individual result
    clustering_coefficient_result_df = pd.DataFrame(list(clustering_coefficient_result.items()),columns=['Edge_Number', 'Clustering_Coefficient'])
    clustering_coefficient_result_df.to_csv('./output/' + metric + '/clustering_coefficient_result_' + metric + '.csv', index=False)
    print("Function calculate_clustering_coefficient() ends at:", time.ctime())

    # Merge the DataFrames on a common column, such as 'Edge_Number'
    merged_df = pd.merge(betweenness_centrality_result_df, pagerank_values_result_df, on='Edge_Number')
    merged_df = pd.merge(merged_df, clustering_coefficient_result_df, on='Edge_Number')
    merged_df = pd.merge(merged_df, degree_centrality_result_df, on='Edge_Number')
    merged_df = pd.merge(merged_df, average_neighbor_degree_result_df, on='Edge_Number')

    merged_df.to_csv('./output/' + metric + '/merged_df_' + metric + '.csv', index=False)

 