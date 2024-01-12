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
    meta_columns = ['node_id', 'name', 'metro_pop', 'latitude', 'longitude', 'country']
    df_meta = pd.read_csv(meta_path)

     # Create empty lists to store the reachability values
    reachability_us = []
    reachability_canada = []
    reachability_other = []
    
    # Iterate over each row in the graph data
    for index, row in df_reachability.iterrows():
        from_node_id = int(row['FromNodeId'])
        to_node_id = int(row['ToNodeId'])

        # Get the country information for the nodes from the df_meta DataFrame
        from_node_country = df_meta.loc[df_meta['node_id'] == from_node_id, 'country'].values
        to_node_country = df_meta.loc[df_meta['node_id'] == to_node_id, 'country'].values

        # Check if the nodes have the same country
        if len(from_node_country) > 0 and len(to_node_country) > 0 and from_node_country == to_node_country:
            # Add the reachability to the specified country
            country = from_node_country[0]  # Assuming both nodes have the same country
            # Calculate reachability for the FromNodeId and ToNodeId pair
            if country == 'United States':
                reachability_us.append(row)
            elif country == 'Canada':
                reachability_canada.append(row)
            else:
                reachability_other.append(row)

        else:
            # Add the reachability to the 'Other' country
            reachability_other.append(row)


    # Create new dataframe for Canada and United States
    df_canada = pd.DataFrame(columns=['FromNodeId', 'ToNodeId', 'Weight'], data=reachability_canada)
    df_united_states = pd.DataFrame(columns=['FromNodeId', 'ToNodeId', 'Weight'], data=reachability_us)
    df_other = pd.DataFrame(columns=['FromNodeId', 'ToNodeId', 'Weight'], data= reachability_other)

    return df_reachability, df_meta, df_canada, df_united_states, df_other

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


