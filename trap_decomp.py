from PolygonPoint import PolygonPoint

def create_polygon_points(obstacles):
    poly_points = []
    for obs in obstacles:
        for tup_pt in obs:
            to_add = PolygonPoint(tup_pt[0], tup_pt[1])
            poly_points.append(to_add)
    return poly_points