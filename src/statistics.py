import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_metric_relationships_across_countries(merged_data, country_name):
    # Analyze relationships between all metrics
    metrics = ['Betweenness_Centrality', 'Pagerank_Values', 'Clustering_Coefficient', 'Degree_Centrality', 'Average_Neighbor_Degree', 'metro_pop']

    for metric in metrics:
        for i, other_metric in enumerate(metrics):
            if metric != other_metric:
                fig, ax = plt.subplots()
                ax.scatter(merged_data[metric], merged_data[other_metric])
                ax.set_xlabel(metric)
                ax.set_ylabel(other_metric)
                plt.tight_layout()
                fig.savefig(f'./output/{country_name}/relationship_{metric}_vs_{other_metric}_{country_name}.png')
                plt.show()


def calculate_correlation(merged_data, country_name):
    metrics = ['Betweenness_Centrality', 'Pagerank_Values', 'Clustering_Coefficient', 'Degree_Centrality', 'Average_Neighbor_Degree', 'metro_pop']
    correlation_matrix = merged_data[metrics].corr()

    # Visualize the correlation matrix as a heatmap
    plt.figure(figsize=(17, 10))  # Increase the figure size
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"fontsize": 9})  # Increase the font size of annotations
    plt.title('Correlation Between Metrics')
    fig = plt.gcf()  # Get the current figure object
    fig.savefig(f'./output/{country_name}/relationship_correlation_heatmap_{country_name}.png', dpi=300)
    plt.show()
