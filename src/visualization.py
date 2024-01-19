import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
import networkx as nx

def visualize_graph(graph, country_name):
    # Remove or replace nan values in the edge data
    graph_with_no_nans = graph.copy()
    graph_with_no_nans.remove_edges_from([(u, v) for u, v, wt in graph.edges(data=True) if pd.isnull(wt)])

    # Create a Plotly figure
    fig = go.Figure()

    # Add nodes to the figure
    for node in graph_with_no_nans.nodes():
        fig.add_trace(go.Scatter(x=[node], y=[node], mode='markers', marker=dict(size=10), name=str(node)))

    # Add edges to the figure
    for u, v in graph_with_no_nans.edges():
        fig.add_trace(go.Scatter(x=[u, v], y=[u, v], mode='lines', line=dict(width=1), name=f'{u}-{v}'))

    # Set layout options
    fig.update_layout(showlegend=False, hovermode='closest')

    # Save the figure as a high-resolution image
    pio.write_image(fig, './output/' + country_name + '/graph.png', width=1200, height=800)

    # Show the figure
    fig.show()


    #######################################networkx#######################################
    # Create a Plotly figure
    fig = go.Figure()

    # Apply a layout algorithm to position the nodes
    pos = nx.spring_layout(graph_with_no_nans)

    # Add nodes to the figure with different colors and sizes
    for node in graph_with_no_nans.nodes():
        fig.add_trace(go.Scatter(x=[pos[node][0]], y=[pos[node][1]], mode='markers', 
                                 marker=dict(size=10, color='blue'), name=str(node)))

    # Add edges to the figure with different thickness and colors
    for u, v in graph_with_no_nans.edges():
        fig.add_trace(go.Scatter(x=[pos[u][0], pos[v][0]], y=[pos[u][1], pos[v][1]], mode='lines', 
                                 line=dict(width=1, color='gray'), name=f'{u}-{v}'))

    # Set layout options
    fig.update_layout(showlegend=False, hovermode='closest')

    # Save the figure as a high-resolution image
    fig.write_image('./output/' + country_name + '/graph-' + country_name +'.png', width=1920, height=1080, scale=2)

    # Show the figure
    fig.show()