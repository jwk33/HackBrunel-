
import networkx as nx


def ReturnOptimalPath(_start_lon_lat, _end_lon_lat, _L):
    nodes = list(G.nodes)
    edges = G.edges


    start_lon_lat = _start_lon_lat 
    end_lon_lat   = _end_lon_lat

    _L = L

    def distance(x, y):
        return (x[0] - y[0])*(x[0] - y[0]) + (x[1] - y[1])*(x[1] - y[1])

    i_min = 0
    min_value = distance(start_lon_lat, nodes[0]) 

    for i in range(len(nodes)):
        if distance(start_lon_lat, nodes[i]):
            i_min = i
            min_value = distance(start_lon_lat, nodes[i])

    start_node = nodes[i_min]

    i_min = 0
    min_value = distance(end_lon_lat, nodes[0]) 

    for i in range(len(nodes)):
        if distance(end_lon_lat, nodes[i]):
            i_min = i
            min_value = distance(end_lon_lat, nodes[i])

    end_node = nodes[i_min]

    lengths_dict = nx.get_edge_attributes(G, 'length')

    M = max(list(lengths_dict.values()))
    lengths = { edges[i] : lengths_dict[edges[i]]/M for i in range(len(edges)) }

    weights = { edge : (L * risks[edge]) + lengths[edge] for i in range(len(edges)) }

    
    H = nx.Graph()
    H.add_nodes_from(G)

    min_weight_for_nodes = {}

    for edge in G.edges:
        u = edge[0]
        v = edge[1]
        
        if (u, v) in min_weight_for_nodes:
            min_weight_for_nodes[(u, v)] = min( min_weight_for_nodes[(u, v)], weights[edge] )

    for key in min_weight_for_nodes.keys():
        H.add_edge(key[0], key[1], min_weight_for_nodes[key])
    

    shortest_path = nx.shortest_path(H, start_node, end_node)
