import pandas as pd
import networkx as nx

def load_data():
    # Implement loading and preprocessing functions here
    pass

def create_graph(df_reachability):
    G = nx.from_pandas_edgelist(df_reachability, 'FromNodeId', 'ToNodeId', ['Weight'], create_using=nx.DiGraph())
    return G

import pandas as pd
import networkx as nx

def load_data():
    # Load reachability.txt
    reachability_path = 'data/reachability.txt'
    reachability_columns = ['FromNodeId', 'ToNodeId', 'Weight']
    df_reachability = pd.read_csv(reachability_path, delimiter='\t', comment='#', header=None, names=reachability_columns)

    # Load reachability-meta.csv
    meta_path = 'data/reachability-meta.csv'
    meta_columns = ['node_id', 'name', 'metro_pop', 'latitude', 'longitude']
    df_meta = pd.read_csv(meta_path)

    return df_reachability, df_meta

def preprocess_data(df_reachability, df_meta):
    # Additional preprocessing steps if needed
    # For example, handling missing values, converting data types, etc.
    # This might include merging the two dataframes based on common columns.

    # Example: Merge on 'FromNodeId' and 'node_id'
    merged_data = pd.merge(df_reachability, df_meta, how='left', left_on='FromNodeId', right_on='node_id')
    
    return merged_data

def create_graph(df_reachability):
    G = nx.from_pandas_edgelist(df_reachability, 'FromNodeId', 'ToNodeId', ['Weight'], create_using=nx.DiGraph())
    return G

# Example usage:
df_reachability, df_meta = load_data()
merged_data = preprocess_data(df_reachability, df_meta)
G = create_graph(merged_data)

# Now you can use the dataframe `merged_data` and the graph `G` for further analysis.
