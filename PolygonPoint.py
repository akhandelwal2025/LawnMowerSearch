class PolygonPoint:
    def __init__(self, x, y, obs_idx):
        self.x = x
        self.y = y

        self.obs_idx = obs_idx #what obstacle it belongs to
        self.upper_ext = 0
        self.lower_ext = 0