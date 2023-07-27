# Probability Calculator Project

Welcome to the **Probability Calculator** project from the **Scientific Computing with Python** course offered by freeCodeCamp. In this project, you will estimate the approximate probability of drawing certain balls randomly from a hat.

## Project Description

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. The task is to calculate the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls. While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate the approximate probability.

For this project, you will create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color.

The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:

- `hat`: A hat object containing balls that should be copied inside the function.
- `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
- `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
- `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability.

## Usage Example

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

## Development and Testing

- Write your code in `prob_calculator.py`. For development, you can use `main.py` to test your code. Click the "run" button, and `main.py` will run.
- The boilerplate includes import statements for the `copy` and `random` modules. Consider using those in your project.

Let's estimate probabilities of drawing balls from a hat using Python! Happy coding!
