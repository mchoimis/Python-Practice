"""
install numpy, scipy, networkx, ipython, matplotlib first.
http://www.slideshare.net/rik0/complex-and-social-network-analysis-in-python
"""
import netowkrx as nx

G = nx.read_dot('small.dot');

pos = nx.spring_layout(G)
lables = dict(zip(G.nodes(), range(len(G))))
nx.draw_networkx_nodes(G, pos, node_color='b', node_size=500, linewidths=2.0)
nx.draw_networkx_labels(G, pos, lables=labels, font_size=18, font_color='w')
nx.draw_networkx_edges(G, pos, width=2.0)
plt.axis('off); None

A = nx.to_numpy_matrix(G)
A * A
