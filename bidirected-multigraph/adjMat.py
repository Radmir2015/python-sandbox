import csv
import pylab
import pydot
import networkx as nx
# from graphviz import Digraph
import matplotlib.pyplot as plt
# from networkx.drawing.nx_pydot import to_pydot
from networkx.drawing.nx_agraph import graphviz_layout, write_dot

routes = csv.reader(open('adjMatrix.csv', 'r'))
routes = list(map(lambda x: list(map(lambda y: '0' if y == '' else y, x[0].split(';'))), list(routes)))

# routes = routes[:len(routes) // 4]

node_names = ['S1', 'S2', 'S3', 'S4', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'T1', 'T2', 'T3', 'T4']

node_to_color = {
    'S': 'blue',
    'W': 'red',
    'O': 'green',
    'T': 'yellow',
}

# routes = list(map(lambda x: x.replace('', '0'), routes))

print('\n'.join(list(map(lambda x: ' '.join(x), routes))))

G = nx.MultiDiGraph()

negative = []

# nx.from_biadjacency_matrix(routes)
for i, r in enumerate(routes):
    for j, n in enumerate(r):
        if int(n) != 0:
            G.add_edge(node_names[i], node_names[j], weight=int(n))
            if int(n) < 0:
                negative.append((node_names[i], node_names[j]))

pos=graphviz_layout(G, prog='circo')
# pos = nx.circular_layout(G, scale=10)

# graphviz_layout(G, prog='neato')
# nx.draw(G)
# pos = nx.spring_layout(G, scale=10)
# nx.draw(G, pos, font_size=8)

edge_color = [ 'red' if edge in negative else 'black' for edge in G.edges() ]
node_color = [ node_to_color[node[0]] for node in G.nodes() ]

# edge_labels = { (u, v): d['weight'] for u, v, d in G.edges(data=True) }
# nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=5)
# nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.3, font_size=5)

# nx.draw(G, pos=pos, edge_color=edge_color, node_color=node_color, node_size=1000, with_labels=True, font_weight='bold')
nx.draw(G, pos=pos, edge_color=edge_color, node_color=node_color, node_size=1000, with_labels=True, font_weight='bold', connectionstyle='arc3, rad = 0.1')
# nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')

# write_dot(G, 'multi.dot')
graph = nx.nx_pydot.to_pydot(G)
graph.write_png('graph_pict.png')

pylab.show()