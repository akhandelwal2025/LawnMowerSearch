import trap_decomp as td
import visualizer
from matplotlib import pyplot as plt

obstacles1 = [
    [(200, 146),(111, 235),(258, 358),(363, 221)],
    [(294, 69),(591, 171),(436, 399),(473, 206)],
    [(150, 21),(22, 261),(193, 456),(516, 451),(676, 138),(529, 28)]
]

obstacles2 = [
    [(425, 53),(172, 150),(319, 273),(260, 146)],
    [(292, 150),(457, 282),(219, 398),(373, 274)],
    [(150, 21),(22, 261),(193, 456),(516, 451),(676, 138),(529, 28)]
]

def sort_obstacles(obstacles):
    to_return = [[tup_pt for tup_pt in obstacle] for obstacle in obstacles] #creating copy
    for obstacle in to_return:
        obstacle.sort(key=lambda pt: pt[0])
    print(to_return)
    return to_return

def main():
    obstacles = obstacles1
    #sorted_obs = sort_obstacles(obstacles)
    poly_points = td.create_sorted_polygon_points(obstacles)
    for idx, poly_pt in enumerate(poly_points):
        td.calc_exts(poly_pt, obstacles)
        td.set_type(poly_pt, obstacles)
        #print(poly_pt.x, poly_pt.y, poly_pt.type, poly_pt.obs_idx_tup)
        td.calc_visibility(poly_pt, poly_points, idx, obstacles)
        print(poly_pt.x, poly_pt.y, poly_pt.type, [(pt.x, pt.y)for pt in poly_pt.visible])
    visualizer.graph_obstacles(obstacles)
    visualizer.graph_edges(poly_points)

if __name__ == '__main__':
    main()