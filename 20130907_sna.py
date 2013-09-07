"""
install numpy, scipy, networkx, ipython, matplotlib first.
http://www.slideshare.net/rik0/complex-and-social-network-analysis-in-python
"""
import networkx as nx

G = nx.erdos_renyi_graph(15, 0.2)
p = nx.shortest_path(G, 6, 11)

pos = nx.spring_layout(G); # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_color='#6E8EBD', node_size=500, linewidths=2.0);
nx.draw_networkx_lables(G, pos, font_size=18, font_color='w');
nx.draw_networks_edges(G, pos, width=2.0, style='dotted');
nx.draw_networks_edges(G, pos, edgelist=zip(p, p[1:]), width=2.0, edge_color='r');
plt.axis('off'); None

nx.average_shortest_path_length(G)
