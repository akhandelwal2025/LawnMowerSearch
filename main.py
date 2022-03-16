import trap_decomp as td
import visualizer

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

def main():
    poly_points = td.create_polygon_points(obstacles1)
    #for pt in poly_points:
    #    print(str(pt.x) + "  " + str(pt.y))
    visualizer.graph_obstacles(obstacles1)

if __name__ == '__main__':
    main()