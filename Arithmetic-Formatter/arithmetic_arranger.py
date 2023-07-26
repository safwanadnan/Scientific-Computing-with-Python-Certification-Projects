def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Check if the number of problems exceeds the limit of five
    if len(problems) > 5:
        return "Error: Too many problems."

    # Step 2: Initialize empty lists for each line of the arranged problems
    top_line = []
    bottom_line = []
    separator_line = []
    result_line = []

    # Step 3: Process each problem in the list
    for problem in problems:
        # Split the problem into the left operand, operator, and right operand
        operand1, operator, operand2 = problem.split()

        # Step 3a: Check if the operator is valid (+ or -)
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Step 3b: Check if both operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Step 3c: Check if any operand exceeds four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Step 3d: Determine the length of the longest operand
        max_length = max(len(operand1), len(operand2))

        # Step 3e: Calculate the result of the arithmetic operation if show_answers is True
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line.append(result.rjust(max_length + 2))

        # Step 3f: Add spaces to the components to align them properly
        space = ' ' * 4  # Four spaces
        top_line.append(operand1.rjust(max_length + 2))
        bottom_line.append(operator + ' ' + operand2.rjust(max_length))
        separator_line.append('-' * (max_length + 2))

    # Step 4: Combine the components into a single string with proper spacing
    arranged_problems = '    '.join(top_line) + '\n' + \
                        '    '.join(bottom_line) + '\n' + \
                        '    '.join(separator_line)

    # Step 5: Include the result line if show_answers is True
    if show_answers:
        arranged_problems += '\n' + '    '.join(result_line)

    # Step 6: Return the final arranged string
    return arranged_problems
