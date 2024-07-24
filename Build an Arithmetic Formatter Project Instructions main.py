def arithmetic_arranger(problems, val=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    operations = list(map(lambda x: x.split()[1], problems))
    if not all(op in ['+', '-'] for op in operations):
        return "Error: Operator must be '+' or '-'."

    numbers = []
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda x: len(x) <= 4, numbers)):
        return "Error: Numbers cannot be more than four digits."

    top_row = ''
    bottom_row = ''
    dashes = ''
    solutions = ''
    for i, problem in enumerate(problems):
        num1, op, num2 = problem.split()
        space_width = max(len(num1), len(num2)) + 2

        top_row += num1.rjust(space_width)
        bottom_row += op + num2.rjust(space_width - 1)
        dashes += '-' * space_width
        if op == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        solutions += result.rjust(space_width)

        if i < len(problems) - 1:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems
