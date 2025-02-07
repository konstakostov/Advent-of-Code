from itertools import product


def create_operator_combinations(num_combination, operators):
    combinations = [list(comb) for comb in product(operators, repeat=num_combination)]
    return combinations


def evaluate_expression(expression):
    expression_result = expression[0]

    for x in range(1, len(expression), 2):
        operator = expression[x]
        next_number = expression[x + 1]
        if operator == "+":
            expression_result += next_number
        elif operator == "*":
            expression_result *= next_number

    return expression_result


OPERATORS = [
    "+",
    "*",
    ""
]
equations = []

with open("bridge_repair_input.txt", "r") as file:
    for line in file:
        values = [int(x) for x in line.replace(":", "").split()]

        equations.append(values)

sum_equations = 0


def concat_equations(expression):
    indices = [index for index, value in enumerate(expression) if value == ""]

    for index in reversed(indices):
        expression[index + 1] = int(str(expression[index - 1]) + str(expression[index + 1]))
        expression.pop(index - 1)
        expression.pop(index - 1)

    return expression


for equation in equations:
    result = equation[0]
    numbers = equation[1:]

    equation_combination_num = (len(numbers) - 1) * (len(OPERATORS) - 2)
    equation_combinations = create_operator_combinations(equation_combination_num, OPERATORS)

    all_equation_version = []

    current_equation = numbers.copy()

    for ec in range(len(equation_combinations) - 1, -1, -1):
        for i in range(len(equation_combinations[ec]) - 1, -1, -1):
            current_equation.insert(i + 1, equation_combinations[ec][i])

        all_equation_version.append(current_equation)
        current_equation = numbers.copy()

    for eq in all_equation_version:
        if "" in eq:
            eq = concat_equations(eq)

        eq_result = evaluate_expression(eq)

        if eq_result == result:
            sum_equations += eq_result
            # print(eq)
            # print(eq_result)
            break

print(sum_equations)