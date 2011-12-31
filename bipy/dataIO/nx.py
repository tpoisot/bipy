from ..bipartite_class import *
import networkx as nx


def nxImport(nxg,name=''):
    if not nx.algorithms.bipartite.is_bipartite(nxg):
        print 'This graph is not bipartite'
        return 0
    else:
        X,Y = nx.algorithms.bipartite.sets(nxg)
        top_nodes = list(Y)
        bottom_nodes = list(X)
        W = np.zeros((len(top_nodes),len(bottom_nodes)))
        for ed in nxg.edges_iter():
            sp1 = ed[0]
            sp2 = ed[1]
            if sp1 in top_nodes:
                W[top_nodes.index(sp1)][bottom_nodes.index(sp2)] = 1
            else:
                W[top_nodes.index(sp2)][bottom_nodes.index(sp1)] = 1
        Bip = bipartite(W)
        Bip.name = name
        Bip.up_names = top_nodes
        Bip.low_names = bottom_nodes
        return Bip
