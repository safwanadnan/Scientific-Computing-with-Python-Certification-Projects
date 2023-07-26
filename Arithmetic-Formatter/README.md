# Arithmetic Formatter Project

Welcome to the **Arithmetic Formatter** project as part of the **Scientific Computing with Python** course. In this project, you will create a Python function that arranges arithmetic problems vertically and side-by-side, just like students do in primary school.

## Problem Description

Students often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

```
  235
+  52
-----
```

Your task is to implement a function that receives a list of arithmetic problems as strings and returns the problems arranged vertically and side-by-side. The function can optionally take a second argument, and when set to True, it will display the answers as well.

## Examples

Function Call:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules

1. The function will return the correct conversion if the supplied problems are properly formatted; otherwise, it will return a meaningful error message.

2. Situations that will return an error:

   - If there are too many problems supplied to the function (limit: five).
   - The function only accepts addition (+) and subtraction (-) operators. Multiplication and division will return an error.
   - Each number (operand) should only contain digits.
   - Each operand has a maximum of four digits in width.

3. If the user supplies the correct format of problems, the conversion will follow these rules:

   - There should be a single space between the operator and the longest of the two operands.
   - Both operands will be in the same order as provided (the first will be the top one, and the second will be the bottom).
   - Numbers should be right-aligned.
   - There should be four spaces between each problem.
   - There should be dashes at the bottom of each problem.

## Development and Testing

- Write your code in `arithmetic_arranger.py`.
- For development, you can use `main.py` to test your `arithmetic_arranger()` function. Click the "run" button, and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We are running the tests from `test_module.py` in `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively, you may run the tests by inputting `pytest` in the console.

Let's get started on arranging arithmetic problems like a pro! Happy coding!
