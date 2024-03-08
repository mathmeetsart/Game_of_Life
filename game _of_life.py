import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to count the number of neighbors for each cell
def count_neighbors(universe):
    """
    Calculates the number of live neighbors for each cell in a Game of Life universe.

    Args:
        universe (numpy.ndarray): A 2D NumPy array representing the current state of the universe.

    Returns:
        numpy.ndarray: A 2D NumPy array containing the neighbor counts for each corresponding cell.
    """

    # Get the dimensions of the universe
    rows, cols = universe.shape

    # Initialize an array to store the counts
    neighbors_count = np.zeros_like(universe)

    # Loop through each cell in the universe
    for i in range(rows):
        for j in range(cols):
            # Count neighbors (use slicing to handle boundary conditions)
            neighbors_count[i, j] = np.sum(universe[i-1:i+2, j-1:j+2]) - universe[i, j]

    return neighbors_count


# Function to update the universe based on the rules of the game
def update_universe(universe):
    """
    Applies the rules of Conway's Game of Life to update the universe to the next generation.

    Args:
        universe (numpy.ndarray): A 2D NumPy array representing the current state of the universe.

    Returns:
        numpy.ndarray: A 2D NumPy array representing the updated state of the universe.
    """

    # Count the number of neighbors for each cell
    neighbors_count = count_neighbors(universe)

    # Create a copy of the universe to modify in place
    new_universe = np.copy(universe)

    # Get the dimensions of the universe
    rows, cols = universe.shape

    # Loop through each cell in the universe
    for i in range(rows):
        for j in range(cols):
            # Apply Conway's Game of Life rules:
            if universe[i, j] == 1:  # Cell is alive
                if neighbors_count[i, j] < 2 or neighbors_count[i, j] > 3:
                    new_universe[i, j] = 0  # Cell dies
            else:  # Cell is dead
                if neighbors_count[i, j] == 3:
                    new_universe[i, j] = 1  # Cell becomes alive

    return new_universe


# Function to update the plot
def update_plot(frame, img, universe):
    """
    Updates the animated plot with the next generation of the Game of Life.

    Args:
        frame (int): The current frame number of the animation.
        img (matplotlib.image.AxesImage): The image object used for the plot.
        universe (numpy.ndarray): The 2D NumPy array representing the current universe state.

    Returns:
        matplotlib.image.AxesImage: The updated image object.
    """

    # Update the universe to the next generation
    universe[:] = update_universe(universe)

    # Update the image data
    img.set_array(universe)

    return img,


# Seeds for different patterns
SEEDS = {
    # Various predefined patterns for the Game of Life
    # You can uncomment and use any of these seeds or define your own
    # Format: Each pattern is represented as a list of lists containing 0s and 1s
    
    "glider": [
        [0, 1, 0],   #3*3
        [0, 0, 1],
        [1, 1, 1] 
    ],
    "eater with glider": [
        [0, 0, 0, 0, 0, 1, 0],   #7*7
        [0, 0, 0, 0, 0, 0, 1],   # Glider at the right
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],   # Eater at the left
        [0, 1, 1, 0, 0, 0, 0]
    ],
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],   #8*3
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [
        [1, 1, 0],   #3*3
        [1, 0, 1], 
        [0, 1, 0]
    ],
    "r_pentomino": [
        [0, 1, 1],   #3*3
        [1, 1, 0], 
        [0, 1, 0]
    ],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],   #8*3
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [
        [1, 1, 0, 0],   #4*4
        [1, 1, 0, 0], 
        [0, 0, 1, 1], 
        [0, 0, 1, 1]
    ],
    "acorn": [
        [0, 1, 0, 0, 0, 0, 0],  #7*3
        [0, 0, 0, 1, 0, 0, 0], 
        [1, 1, 0, 0, 1, 1, 1]
    ],
    "spaceship": [
        [0, 0, 1, 1, 0],    #5*4
        [1, 1, 0, 1, 1], 
        [1, 1, 1, 1, 0], 
        [0, 1, 1, 0, 0]
    ],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],   #8*6
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],    #5*5
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
    "glider_gun": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #40*11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ], 
    "toad": [
        [0, 0, 0, 0, 0],    #5*4
        [0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ], 
    "thunderbird": [
        [1, 1, 1],    #3*5
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
}

# Initialize universe (random or using a seed)
#UNIVERSE = np.zeros((128, 128))  # Initialize with all cells dead
UNIVERSE = np.random.randint(2, size=(128, 128))  # For a random starting state

# Set seed for an interesting pattern
#UNIVERSE[50:61, 10:50] = SEEDS["glider_gun"]

# Animation parameters
ITERATIONS = 100  # Number of generations to simulate
SPEED = 10  # Animation speed (interval in milliseconds)

# Plotting
fig, ax = plt.subplots()
img = ax.imshow(UNIVERSE, cmap='binary')  # Initial plot of the universe
ani = animation.FuncAnimation(fig, update_plot, fargs=(img, UNIVERSE), frames=ITERATIONS, interval=SPEED, blit=True)

# Optionally save animation as an MP4 file
ani.save('game_of_life_animation.mp4', writer='imagemagick', fps=5)

plt.show()  # Display the animation