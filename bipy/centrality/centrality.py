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


def degree_c(w):
    dc_top = w.generality / float(w.losp)
    dc_bot = w.vulnerability / float(w.upsp)
    return [dc_top, dc_bot]

def between_c(n):
    return 0

def close_c(n):
    return 0