from src.data_loading import load_data, create_graph
from src.graph_analysis import calculations
from src.visualization import visualize_graph
from src.statistics import visualize_metric_relationships_across_countries,calculate_correlation
import time
import pandas as pd


# Load data
df_reachability, df_meta, df_canada, df_united_states, df_other = load_data()

# Create graph
G = create_graph(df_reachability)
G_CANADA = create_graph(df_canada)
G_UNITED_STATES = create_graph(df_united_states)
G_OTHER = create_graph(df_other)

#  Perform analysis
merged_df_ALL=calculations(G,"ALL",df_meta)

################################
##CANADA
################################

# Perform analysis
merged_df_CANADA=calculations(G_CANADA,"CANADA",df_meta)


################################
##UNITED_STATES
################################

# Perform analysis
merged_df_UNITED_STATES=calculations(G_UNITED_STATES,"USA",df_meta)

#################################
##OTHERS
################################
# Perform analysis
merged_df_OTHER=calculations(G_OTHER,"OTHERS",df_meta)

# Visualize results
visualize_graph(G, "ALL")
visualize_graph(G_CANADA, "CANADA")
visualize_graph(G_UNITED_STATES, "USA")
visualize_graph(G_OTHER, "OTHERS")


##############Statistics################

visualize_metric_relationships_across_countries(merged_df_ALL, "ALL")
visualize_metric_relationships_across_countries(merged_df_CANADA, "CANADA")
visualize_metric_relationships_across_countries(merged_df_UNITED_STATES, "USA")
visualize_metric_relationships_across_countries(merged_df_OTHER, "OTHERS")



##############corrolation################
# merged_df_path = 'output/ALL/merged_df_ALL.csv'
# merged_df_ALL = pd.read_csv(merged_df_path)
calculate_correlation(merged_df_ALL, "ALL")