class PolygonPoint:
    UNDEFINED = 0
    IN = 1
    MIDDLE = 2
    OUT = 3
    BOUNDARY = 4
    def __init__(self, x, y, obs_idx):
        self.x = x
        self.y = y

        self.obs_idx = obs_idx #what obstacle it belongs to
        self.upper_ext = 0
        self.lower_ext = 0

        self.type = self.UNDEFINED

        self.visible = []