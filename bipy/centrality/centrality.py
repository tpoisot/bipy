class centrality_level:
    def __init__(self):
        self.top = []
        self.bottom = []

class centrality:
    def __init__(self,web):
        self.degree = centrality_level()
        c_degr = degree_c(web)
        self.degree.top = c_degr[0]
        self.degree.bottom = c_degr[1]

#TODO: use the networkX functions once the nxExport method is done