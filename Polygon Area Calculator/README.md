# Polygon Area Calculator Project

Welcome to the **Polygon Area Calculator** project from the **Scientific Computing with Python** course offered by freeCodeCamp. In this project, you will utilize object-oriented programming to create a `Rectangle` class and a `Square` class. The `Square` class will be a subclass of `Rectangle` and inherit methods and attributes.

## Project Description

### Rectangle Class

When a `Rectangle` object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:

1. `set_width`: Sets the width attribute of the rectangle.
2. `set_height`: Sets the height attribute of the rectangle.
3. `get_area`: Returns the area of the rectangle (width * height).
4. `get_perimeter`: Returns the perimeter of the rectangle (2 * width + 2 * height).
5. `get_diagonal`: Returns the diagonal of the rectangle ((width ** 2 + height ** 2) ** 0.5).
6. `get_picture`: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height, and the number of "*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
7. `get_amount_inside`: Takes another shape (square or rectangle) as an argument and returns the number of times the passed-in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a `Rectangle` is represented as a string, it should look like: `Rectangle(width=5, height=10)`.

### Square Class

The `Square` class should be a subclass of `Rectangle`. When a `Square` object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the `Rectangle` class.

The `Square` class should be able to access the `Rectangle` class methods but should also contain a `set_side` method. If an instance of a `Square` is represented as a string, it should look like: `Square(side=9)`.

Additionally, the `set_width` and `set_height` methods on the `Square` class should set both the width and height.

### Usage Example

```python
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

That code should return:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****
```

## Development and Testing

- Write your code in `shape_calculator.py`. For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button, and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

Let's calculate areas of polygons using Python's object-oriented programming! Happy coding!
