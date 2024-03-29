# Time Calculator Project

Welcome to the **Time Calculator** project as part of the **Scientific Computing with Python** course. In this project, you will create a Python function named `add_time` that calculates the result of adding a duration time to a given start time in the 12-hour clock format (ending in AM or PM). The function can also take an optional starting day of the week as input.

## Problem Description

The `add_time` function takes the following parameters:

- `start`: A start time in the 12-hour clock format (ending in AM or PM).
- `duration`: A duration time that indicates the number of hours and minutes.
- `starting_day` (optional): A starting day of the week (case insensitive).

The function should add the duration time to the start time and return the result. If the result is on the next day, it should show `(next day)` after the time. If the result is more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional `starting_day` parameter, then the output should also display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

## Examples

```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## Development and Testing

- Write your code in `time_calculator.py`.
- For development, you can use `main.py` to test your `add_time()` function. Click the "run" button, and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

Let's create a handy time calculator with Python! Happy coding!
