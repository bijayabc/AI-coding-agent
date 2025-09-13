# calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else ValueError("Division by zero"),
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            raise ValueError("Empty expression")
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)

                operators.append(token)
            elif token.isdigit() or '.' in token:
                values.append(float(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self._apply_operator(operators, values)
                operators.pop()  # Remove '('
            else:
                raise ValueError("Invalid token: " + token)

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("Invalid expression")
        return values[0]

    def _apply_operator(self, operators, values):
        if not operators or len(values) < 2:
            raise ValueError("Invalid expression")
        operator = operators.pop()
        b = values.pop()
        a = values.pop()
        try:
            result = self.operators[operator](a, b)
            if isinstance(result, ValueError):
                raise result
            values.append(result)
        except Exception as e:
            raise ValueError(str(e))
