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
    plt.show()