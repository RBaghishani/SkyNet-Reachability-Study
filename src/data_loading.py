import pandas as pd
import networkx as nx
import pickle
import time

def load_data():
    # Load reachability.txt
    reachability_path = 'data/reachability.txt'
    reachability_columns = ['FromNodeId', 'ToNodeId', 'Weight']
    df_reachability = pd.read_csv(reachability_path, delimiter=' ', comment='#', header=None, names=reachability_columns, dtype={'FromNodeId': int, 'ToNodeId': int, 'Weight': float})

    # Split the 'FromNodeId' column based on space and keep the first part
    # df_reachability['FromNodeId'] = df_reachability['FromNodeId'].str.split().str[0]

    # Convert the 'FromNodeId' column to integer
    # df_reachability['FromNodeId'] = df_reachability['FromNodeId'].astype(int)

    # Load reachability-meta.csv
    meta_path = 'data/reachability-meta.csv'
    meta_columns = ['node_id', 'name', 'metro_pop', 'latitude', 'longitude']
    df_meta = pd.read_csv(meta_path)

    return df_reachability, df_meta

def preprocess_data(df_reachability, df_meta):
    # Merge the dataframes
    merged_data = pd.merge(df_reachability, df_meta, how='left', left_on='FromNodeId', right_on='node_id')

    return merged_data

def create_graph(df_reachability):
    print("Function create_graph() starts at:", time.ctime())
    G = nx.from_pandas_edgelist(df_reachability, 'FromNodeId', 'ToNodeId', ['Weight'], create_using=nx.DiGraph())
    # Load the graph from the file

    # with open('graph.pkl', 'rb') as f:
    #    G = pickle.load(f)
    # Save the graph to a file (e.g., graph.pkl)
    with open('graph.pkl', 'wb') as f:
        pickle.dump(G, f)
    print("Function create_graph() ends at:", time.ctime())

    return G

# Save Graph
# df_reachability, df_meta = load_data()
# merged_data = preprocess_data(df_reachability, df_meta)
# G = create_graph(merged_data)


# Now you can use the dataframe `merged_data` and the graph `G_loaded` for further analysis.


