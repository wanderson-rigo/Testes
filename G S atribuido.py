class Expr:
    def __init__(self, expr=None, op=None, term=None):
        self.expr = expr
        self.op = op
        self.term = term

    def generate_assembly(self):
        assembly_code = ""
        if self.expr is not None:
            assembly_code += self.expr.generate_assembly()
        if self.op == "+":
            assembly_code += self.term.generate_assembly()
            assembly_code += f"ADD R{self.expr.register}, R{self.term.register}, R{self.expr.register}"
        return assembly_code


class Term:
    def __init__(self, term=None, op=None, factor=None):
        self.term = term
        self.op = op
        self.factor = factor

    def generate_assembly(self):
        assembly_code = ""
        if self.term is not None:
            assembly_code += self.term.generate_assembly()
        if self.op == "*":
            assembly_code += self.factor.generate_assembly()
            assembly_code += f"MUL R{self.term.register}, R{self.factor.register}, R{self.term.register}"
        return assembly_code


class Factor:
    def __init__(self, expression=None):
        self.expression = expression

    def generate_assembly(self):
        assembly_code = ""
        if self.expression.startswith("("):
            expr = self.expression[1:-1]
            assembly_code += Expr(expr).generate_assembly()
        else:
            assembly_code += self.expression
        return assembly_code


def translate(expression):
    ast = Expr()
    ast.expr = Term()
    ast.expr.term = Factor()
    ast.expr.term.factor = Factor(expression)
    return "Resultado: " + ast.generate_assembly()


assembly_code = translate("5 + 3")
print(assembly_code)  # Resultado: ADD R0, 5, MUL R1, 3, 2
