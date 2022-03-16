from matplotlib import pyplot as plt

def graph_obstacles(obstacles):
    for obstacle in obstacles:
        obs_x = []
        obs_y = []
        for num in range(len(obstacle)+1):
            elem = obstacle[num%len(obstacle)]
            obs_x.append(elem[0])
            obs_y.append(elem[1])
        plt.plot(obs_x, obs_y)

def graph_edges(poly_points):
    for pt in poly_points:
        x_list = [pt.x, pt.x]
        if pt.upper_ext >= 0:
            y_list = [pt.y, pt.upper_ext]
            plt.plot(x_list, y_list, color="red")
        if pt.lower_ext >= 0:
            y_list = [pt.y, pt.lower_ext]
            plt.plot(x_list, y_list, color="blue")
    plt.show()
    
            

