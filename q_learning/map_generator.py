import sys
import numpy as np

# Check if a csv file is passed as an argument. If so load it, otherwise create it in numpy
if len(sys.argv) > 1:
    maze_data = np.loadtxt(sys.argv[1], delimiter=',', dtype=int)
    assert maze_data.shape[0] == maze_data.shape[1], "Map must be square"
else:
    # Recall the map starts with ALL walls up (perimeter and interior) and at each cell
    # we define which walls get taken down (1=North, 2=East, 4=South, 8=West). The agent
    # starts at the top left corner (0,0) and the goal is at the bottom right corner (n-1,n-1)
    maze_data = np.zeros((5, 5), dtype=int)
    # maze_data[0, 0] = 6
    # maze_data[1, 0] = 2
    # maze_data[2, 0] = 4
    # maze_data[3, 0] = 6
    # maze_data[4, 0] = 4
    # maze_data[4, 1] = 8
    # maze_data[3, 1] = 8
    # maze_data[2, 1] = 4
    # maze_data[1, 1] = 2
    # maze_data[0, 1] = 6
    # maze_data[0, 2] = 6
    # maze_data[1, 2] = 2
    # maze_data[2, 2] = 4
    # maze_data[4, 2] = 8
    # maze_data[4, 3] = 12
    # maze_data[3, 3] = 12
    # maze_data[2, 3] = 4
    # maze_data[1, 3] = 2
    # maze_data[0, 3] = 6
    # maze_data[0, 4] = 2
    # maze_data[1, 4] = 2
    # maze_data[3, 4] = 2
    '''
    # Here is the maze we just created
    +--+--+--+--+--+
    |        |     |
    +  +--+  +  +  +
    |              |
    +  +--+  +--+--+
    |              |
    +  +--+  +--+--+
    |              |
    +  +--+  +  +  +
    |        |     |
    +--+--+--+--+--+
    '''

    maze_data[0, 0] = 6
    maze_data[1, 0] = 6
    maze_data[2, 0] = 6
    maze_data[3, 0] = 6
    maze_data[4, 0] = 4
    maze_data[0, 1] = 4
    maze_data[2, 1] = 4
    maze_data[4, 1] = 4
    maze_data[0, 2] = 4
    maze_data[1, 2] = 6
    maze_data[2, 2] = 6
    maze_data[3, 2] = 4
    maze_data[4, 2] = 4
    maze_data[0, 3] = 6
    maze_data[2, 3] = 4
    maze_data[3, 3] = 2
    maze_data[4, 3] = 4
    maze_data[0, 4] = 2
    maze_data[3, 4] = 2
    '''
    # Here is the maze we just created
    +--+--+--+--+--+
    |              |
    +  +  +  +  +  +
    |  |  |  |  |  |
    +  +--+  +--+  +
    |  |        |  |
    +  +  +  +  +  +
    |     |  |     |
    +  +--+  +--+  +
    |     |  |     |
    +--+--+--+--+--+
    '''

# Note that the code expects it a certain way so we pre-process it here.

# New note, the below code wouldn't actually change the map orientation.
# I accidentally left it in from previous versions of the file. I'm leaving
# it here however to avoid confusion. 
maze_data = np.swapaxes(maze_data, 0, 1)
maze_data = maze_data.T

save_map_name = 'maze2d_regular_5x5_v2.npy'
np.save(save_map_name, maze_data)
