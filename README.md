# Game of Life

Welcome to the Game of Life repository! Explore the fascinating world of cellular automata and emergent behavior.
<br/><br/>

## Description

The Game of Life, invented by mathematician John Conway in 1970, is a cellular automaton that simulates the evolution of life-like patterns on a grid. It consists of a grid of cells, each of which can be in one of two states: alive or dead. The game evolves according to simple rules based on the number of neighboring alive cells.

The rules are as follows:
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

These simple rules give rise to a wide variety of visually intriguing patterns, ranging from simple oscillators and spaceships to complex structures like gliders and glider guns. Some of the most famous patterns include the glider, blinker, and pulsar.

For more information, you can refer to the [Wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
<br/><br/>

## Visual Appeal and Artistic Representation

The Game of Life produces a wide variety of visually intriguing patterns, ranging from simple oscillators and spaceships to complex structures like gliders and glider guns. Artists and mathematicians have been fascinated by the emergent behavior of the game, using it as inspiration for various forms of artistic expression, including digital art and sculptures.
<br/><br/>

## Applications

Beyond its aesthetic appeal, the Game of Life has practical applications in various fields, including computer science, biology, and artificial intelligence. It serves as a model for studying complex systems, pattern formation, and emergent behavior.
<br/><br/>

## Code

Explore the code used to simulate the Game of Life. The code is written in Python and utilizes libraries such as matplotlib and numpy.

### Requirements

- Python 3.12
- ImageMagick (only for saving the animation)
- NumPy
- Matplotlib

### Usage

1. Clone this repository or download the `game_of_life_animation.py` file.
2. Make sure you have Python and the required dependencies installed.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `game_of_life_animation.py`.
5. Run the script using the following command:

    ```bash
    python game_of_life_animation.py
    ```

6. The script will generate an animation of Conway's Game of Life and display it in a new window.
   
### Customization

You can customize the behavior and appearance of the animation by modifying the parameters in the script:

### Generating the Universe

- To initialize the universe with a **random state**, uncomment the line:

    ```python
    UNIVERSE = np.random.randint(2, size=(128, 128))
    ```

- To use a **predefined pattern (seed)**, uncomment one of the patterns provided in the `SEEDS` dictionary. For example:

    ```python
    # Set seed for an interesting pattern
    UNIVERSE[50:61, 10:50] = SEEDS["glider_gun"]
    ```

### Mechanics of Generating a Random Universe

If you want to **generate a random universe of a different size**, you can modify the dimensions of the `UNIVERSE` array:

```python
UNIVERSE = np.random.randint(2, size=(rows, cols))
```
Replace rows and cols with the desired dimensions.

### Placing a Seed

You can place a seed (predefined pattern) anywhere in the universe by modifying the indices in the `UNIVERSE` array:

```python
UNIVERSE[start_row:end_row, start_col:end_col] = SEEDS["your_seed_name"]
```
Replace `start_row`, `end_row`, `start_col`, and `end_col` with the desired indices to specify the location of the seed.

The script includes various predefined patterns for initializing the Game of Life universe, such as glider, glider gun, beacon, etc. You can look in the dictionary and use any of these seeds or define your own.

### Other Custamizations

- `ITERATIONS`: Number of generations to simulate.
- `SPEED`: Animation speed, specified in milliseconds.

### Saving the Animation

You can save the animation as an MP4 file by uncommenting the following line in the script:

```python
# ani.save('game_of_life_animation.mp4', writer='imagemagick', fps=5)
```
This line saves the animation with the specified filename and frames per second (fps).
<br/><br/>

## Sample Images

Below are some sample images generated using the code in this repository:

1. ![Image 1](image1.png)
2. ![Image 2](image2.png)
3. ![Image 3](image3.png)

Explore the code, create your own simulations, and witness the fascinating dynamics of the Game of Life!
<br/><br/>

## Contribution Guidelines

Contributions to this project are welcome! If you would like to contribute, please follow these guidelines:
- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes
- Test your changes thoroughly
- Submit a pull request
<br/><br/>

## Contact Information

For questions, feedback, or collaboration opportunities, feel free to reach out to me:
- Email: mathmeetsart01@gmail.com
- Instagram: [art_meets_math](https://www.instagram.com/art_meets_math/)

---

This repository is a subrepository of [Math Meets Art](https://www.instagram.com/art_meets_math/), which is aimed at making math accessible, intriguing, and visually captivating for everyone. Through this platform, I aim to demonstrate that math is not merely about numbers but a realm of boundless creativity and discovery. Each piece of art presented here also offers an opportunity to learn and appreciate the underlying mathematical concepts.
