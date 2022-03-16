from PolygonPoint import PolygonPoint

def create_sorted_polygon_points(obstacles):
    poly_points = []
    for obs_idx, obs in enumerate(obstacles):
        for tup_pt in obs:
            to_add = PolygonPoint(tup_pt[0], tup_pt[1], obs_idx)
            poly_points.append(to_add)
    poly_points.sort(key=lambda pt: pt.x)
    return poly_points

#calcs y-coord of upper, lower exts and sets it in poly_pt
def calc_exts(poly_pt, obstacles):
    intersects = [[], []] #first list = upper, second list = lower
    for obs_idx, obs in enumerate(obstacles):
        x = poly_pt.x
        y = poly_pt.y
        for num in range(len(obs)):
            node1 = obs[num]
            node2 = obs[(num+1)%len(obs)]
            if (x > node1[0] and x < node2[0]) or (x > node2[0] and x < node1[0]):
                m = (node2[1]-node1[1])/(node2[0]-node1[0])
                intersect = m*(x-node1[0]) + node1[1]
                if intersect > y:
                    intersects[0].append(intersect) 
                else:
                    intersects[1].append(intersect)

    if len(intersects[0]) == 0 or len(intersects[0])%2 == 0:
        poly_pt.upper_ext = -1 #upper ext doesn't exist
    else:
        min_upper = intersects[0][0]
        for upper_intersect in intersects[0]:
            if upper_intersect < min_upper:
                min_upper = upper_intersect
        poly_pt.upper_ext = min_upper


    if len(intersects[1]) == 0 or len(intersects[1])%2 == 0:
        poly_pt.lower_ext = -1 #lower ext doesn't exist
    else:
        min_lower = intersects[1][0]
        for lower_intersect in intersects[1]:
            if lower_intersect > min_lower:
                min_lower = lower_intersect
        poly_pt.lower_ext = min_lower  

    print(x, y)
    print(intersects[0])
    print(intersects[1])  