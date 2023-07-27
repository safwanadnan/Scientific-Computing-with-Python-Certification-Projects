class Rectangle:
  # Rectangle class represents a rectangle shape

  def __init__(self, width: int, height: int):
    # Initializes a Rectangle object with given width and height
    self._width = width
    self._height = height

  @property
  def width(self) -> int:
    # Getter method for width attribute
    return self._width

  @width.setter
  def width(self, value: int):
    # Setter method for width attribute
    if value <= 0:
      raise ValueError("Width must be a positive number.")
    self._width = value

  @property
  def height(self) -> int:
    # Getter method for height attribute
    return self._height

  @height.setter
  def height(self, value: int):
    # Setter method for height attribute
    if value <= 0:
      raise ValueError("Height must be a positive number.")
    self._height = value

  def __str__(self) -> str:
    # String representation of a Rectangle object
    return f"Rectangle(width={self._width}, height={self._height})"

  def set_width(self, width: int):
    # Updates the width of the rectangle
    self.width = width

  def set_height(self, height: int):
    # Updates the height of the rectangle
    self.height = height

  def get_area(self) -> int:
    # Calculates and returns the area of the rectangle
    return self._width * self._height

  def get_perimeter(self) -> int:
    # Calculates and returns the perimeter of the rectangle
    return 2 * (self._width + self._height)

  def get_diagonal(self) -> float:
    # Calculates and returns the diagonal length of the rectangle using Pythagorean theorem
    return (self._width**2 + self._height**2)**0.5

  def get_picture(self) -> str:
    # Returns a string representation of the rectangle using '*' for each cell
    if self._width > 50 or self._height > 50:
      return "Too big for picture."
    picture = ""
    for _ in range(self._height):
      picture += "*" * self._width + "\n"
    return picture

  def get_amount_inside(self, shape: "Rectangle") -> int:
    # Calculates and returns the number of times the passed shape can fit inside the rectangle
    if not isinstance(shape, Rectangle):
      raise TypeError("Shape must be an instance of Rectangle.")
    width_ratio = self._width // shape.width
    height_ratio = self._height // shape.height
    return width_ratio * height_ratio


class Square(Rectangle):
  # Square class represents a square shape, which is a specific type of rectangle

  def __init__(self, side: int):
    # Initializes a Square object with a given side length
    super().__init__(
      side, side
    )  # Calls the parent class (Rectangle) constructor with equal width and height

  @property
  def side(self) -> int:
    # Getter method for the side attribute (same as the width of the square)
    return self.width

  @side.setter
  def side(self, value: int):
    # Setter method for the side attribute (updates both width and height of the square)
    self.width = value
    self.height = value

  def __str__(self) -> str:
    # String representation of a Square object
    return f"Square(side={self.width})"

  def set_side(self, side: int):
    # Updates the side length of the square (also updates width and height)
    self.side = side

  @classmethod
  def from_square(cls, side: int) -> "Square":
    # Alternative constructor that creates a square from a side length
    return cls(side)
