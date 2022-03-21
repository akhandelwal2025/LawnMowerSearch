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

def set_type(poly_pt, sorted_obs):
    if(poly_pt.obs_idx == len(sorted_obs)-1):
        poly_pt.type = poly_pt.BOUNDARY
    else:
        obstacle = sorted_obs[poly_pt.obs_idx]
        if obstacle[0][0] == poly_pt.x:
            poly_pt.type = poly_pt.IN
        elif obstacle[-1][0] == poly_pt.x:
            poly_pt.type = poly_pt.OUT
        else:
            poly_pt.type = poly_pt.MIDDLE

def ccw(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) < (B[1]-A[1])*(C[0]-A[0])

def calc_visibility(poly_pt, poly_points, idx, obstacles):
    print("\n")
    print("\n")
    print(poly_pt.x, poly_pt.y)
    expected_pts = 2 if poly_pt.type == poly_pt.IN else 1
    visible_pts = []
    for next_pt in poly_points[idx+1:len(poly_points)]:
        if next_pt.obs_idx == poly_pt.obs_idx:
            continue
        A = (poly_pt.x, poly_pt.y)
        B = (next_pt.x, next_pt.y)
        intersect_obs = False
        for obstacle in obstacles[0:len(obstacles)-1]:
            for num in range(len(obstacle)):
                C = obstacle[num%len(obstacle)]
                D = obstacle[(num+1)%len(obstacle)]
                if A == C or A == D or B == C or B == D:
                    continue
                if ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D):
                    #print(next_pt.x, next_pt.y, "intersects", C, D)
                    intersect_obs = True
                    break
                else:
                    print(next_pt.x, next_pt.y, C, D)
            if intersect_obs:
                break
        if not intersect_obs:
            visible_pts.append(next_pt)
            if expected_pts == 1:
                break
    #print("visible points")
    #print("-----------------------")
    #print([(pt.x, pt.y)for pt in visible_pts])
    if expected_pts == 2:
        fake = PolygonPoint(10000000, 10000000, 0)
        upper_pt = fake #TODO change from fake to smth better
        lower_pt = fake #TODO change from fake to smth better
        for pt in visible_pts:
            if pt.y > poly_pt.y and pt.x < upper_pt.x:
                upper_pt = pt
            if pt.y < poly_pt.y and pt.x < lower_pt.x:
                lower_pt = pt
        poly_pt.visible.append(upper_pt)
        poly_pt.visible.append(lower_pt)
    else:
        if len(visible_pts) != 0:
            poly_pt.visible.append(visible_pts[0])

