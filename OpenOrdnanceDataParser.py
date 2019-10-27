import bs4
import dill
import convertbng.util
import networkx as nx

with open("OSOpenRoads_TL.gml", 'r') as fp:
    sp = bs4.BeautifulSoup(fp.read(), "xml")

road_links = sp.select('road|RoadLink')
road_nodes = sp.select('road|RoadNode')


def location_of_node(node):
    EN = node.pos.text.split(' ')
    long_lat = (0,0)
    
    a = convertbng.util.convert_lonlat(float(EN[0]), float(EN[1]))
    long_lat = (a[0][0], a[1][0])
    return long_lat

location_to_node = {location_of_node(road_node) : road_node for road_node in road_nodes}

node_to_id = {}

G = nx.MultiGraph()
#n = 0
for rd_node in road_nodes:
    G.add_node(location_of_node(rd_node))
    
#    node_to_id[rd_node] = n
    
#    n += 1
c = 0
for rd_link in road_links:
    poss = [float( s) for s in rd_link.posList.text.split(' ')]

    long_lats = convertbng.util.convert_lonlat( poss[0::2], poss[1::2] )

    path = [(long_lats[0][i], long_lats[1][i]) for i in range(len(long_lats))]
    
    _length = rd_link.length
    
    try:
        if location_of_node(rd_link.startNode) == path[0]:
            if c > 100:
                break
            c += 1
            print('good')
    except:
        pass

    if path[0] in G.nodes:
        node1 = path[0]
    else:
        G.add_node(path[0])
        node1 = path[0]


    if path[-1] in G.nodes:
        node2 = path[-1]
    else:
        G.add_node(path[-1])
        node2 = path[-1]


    G.add_edge(node1, node2, points=path, length = _length )


nx.write_gpickle(G, 'road_network.gpickle')
