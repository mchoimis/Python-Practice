from igraph import Graph

def scipy_to_igraph(matrix, directed=True):
    sources, targets = matrix.nonzero()
    weights = matrix[sources, targets]
    return Graph(zip(sources, targets), directed=directed, edge_attrs={'weight': weights})
