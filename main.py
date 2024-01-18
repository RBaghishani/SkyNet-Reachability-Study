from src.data_loading import load_data, create_graph
from src.graph_analysis import calculations
from src.visualization import visualize_graph
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
calculations(G,"ALL")

################################
##CANADA
################################

# Perform analysis
calculations(G_CANADA,"CANADA")


################################
##UNITED_STATES
################################

# Perform analysis
calculations(G_UNITED_STATES,"USA")

#################################
##OTHERS
################################
# Perform analysis
calculations(G_OTHER,"OTHERS")

# Visualize results
visualize_graph(G)
visualize_graph(G_CANADA)
visualize_graph(G_UNITED_STATES)
visualize_graph(G_OTHER)