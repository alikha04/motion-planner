import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.motion_planners.rrt import RRT


def main():
    print("start " + __file__)

    # ====Search Path with RRT====
    obstacleList = [(5, 5, 1), (3, 6, 2), (3, 8, 2), (3, 10, 2), (7, 5, 2),
                    (9, 5, 2), (8, 10, 1)]  # [x, y, radius]
    # Set Initial parameters
    rrt = RRT(
        start=[0, 0],
        goal=[6.0, 10.0],
        rand_area=[-2, 15],
        obstacle_list=obstacleList,
        robot_radius=0.8
    )
    path = rrt.planning(animation=True)

    if path is None:
        print("Cannot find path")
    else:
        print("found path!!")

        # Draw final path
        if True:  # Set to True for animation
            rrt.draw_graph()
            plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')
            plt.grid(True)
            plt.pause(0.01)  # Need for Mac
            plt.show()

if __name__ == '__main__':
    main()
