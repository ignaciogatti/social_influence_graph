import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def get_edge_dict(df, col_to_split, col_to_index, col_to_clean):
    
    df[col_to_clean] = df[col_to_clean].str.replace(r'[\[\]\'\']', '')
    df[col_to_split] = df[col_to_split].str.split(r', ')
    df = df.set_index(col_to_index)
    df = df.transpose()
    author_dict = df.to_dict('list')
    author_dict = {key:value[0] for key, value in author_dict.items()}
    return author_dict


def plot_graph(G, weight_name=None):
    '''
    #G: a networkx G
    #weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None
    colors = [G[u][v]['color'] for u,v in edges]
    
    if weight_name:
        weights = [int(G[u][v][weight_name]) for u,v in edges]
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights)
    else:
        nx.draw_networkx_edges(G, pos, edge_color=colors)
        #nx.draw_networkx(G, pos, edges=edges, with_labels=True, edge_color='k', width=1.0);