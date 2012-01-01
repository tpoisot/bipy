import networkx.algorithms.bipartite.centrality as nabc
import networkx.algorithms.bipartite.basic as nabb

class centrality_level:
    def __init__(self,centr):
        new_top = {}
        new_bot = {}
        for sp_top in centr[0]:
            tval = centr[0][sp_top]
            new_top[sp_top[4:]] = tval
        for sp_bot in centr[1]:
            tval = centr[0][sp_bot]
            new_bot[sp_bot[4:]] = tval
        self.top = new_top
        self.bottom = new_bot

class centrality:
    def __init__(self,web):
        web.nxExport()
        self.degree = centrality_level(deg_c(web.G))
        #self.closeness = centrality_level(clo_c(web.G))
        self.betweenness = centrality_level(bet_c(web.G))

def deg_c(web):
    top = nabb.sets(web)[0]
    bot = nabb.sets(web)[1]
    return [nabc.degree_centrality(web,top),nabc.degree_centrality(web,bot)]

def clo_c(web):
    top = nabb.sets(web)[0]
    bot = nabb.sets(web)[1]
    return [nabc.closeness_centrality(web,top),nabc.closeness_centrality(web,bot)]

def bet_c(web):
    top = nabb.sets(web)[0]
    bot = nabb.sets(web)[1]
    return [nabc.betweenness_centrality(web,top),nabc.betweenness_centrality(web,bot)]