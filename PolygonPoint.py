class PolygonPoint:
    UNDEFINED = 0
    IN = 1
    MIDDLE = 2
    OUT = 3
    BOUNDARY = 4
    def __init__(self, x, y, obs_idx_tup):
        self.x = x
        self.y = y

        self.obs_idx_tup = obs_idx_tup #(obs_idx, pt_idx)
        self.adj_pts = []
        self.upper_ext = 0
        self.lower_ext = 0

        self.type = self.UNDEFINED

        self.visible = []