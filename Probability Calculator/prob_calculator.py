import random
import copy

class Hat:

  def __init__(self, **balls):
    self.contents = []
    for color, count in balls.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      return self.contents

    # Randomly sample balls without replacement
    balls_drawn = random.sample(self.contents, num_balls)

    # Remove the drawn balls from the available contents
    for ball in balls_drawn:
      self.contents.remove(ball)

    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successful_experiments = 0

  for _ in range(num_experiments):
    # Create a copy of the available balls for each experiment
    available_balls = hat.contents.copy()

    # Draw the specified number of balls
    drawn_balls = hat.draw(num_balls_drawn)

    # Count the occurrence of each drawn ball
    drawn_balls_dict = {}
    for ball in drawn_balls:
      drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

    # Check if the drawn balls meet the expected criteria
    success = True
    for color, count in expected_balls.items():
      if drawn_balls_dict.get(color, 0) < count:
        success = False
        break

    # If the criteria are met, increment the count of successful experiments
    if success:
      successful_experiments += 1

    # Restore the available balls for the next experiment
    hat.contents = available_balls

  # Return the estimated probability of success
  return successful_experiments / num_experiments
