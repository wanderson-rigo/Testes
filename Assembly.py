# Gramática:
# Expr -> Expr + Term | Term
# Term -> Term * Factor | Factor
# Factor -> (Expr) | Number

class AssemblyTranslator:
    def __init__(self):
        self.registerCount = 0

    def translate(self, expression):
        return self.Expr(expression)

    def Expr(self, expression):
        if '+' in expression:
            expr, op, term = expression.split()
            return self.Expr(expr) + " " + self.Term(term) + " ADD R" + str(self.registerCount) + ", R" + str(self.registerCount - 1) + ", R" + str(self.registerCount)
        else:
            return self.Term(expression)

    def Term(self, expression):
        if '*' in expression:
            term, op, factor = expression.split()
            return self.Term(term) + " " + self.Factor(factor) + " MUL R" + str(self.registerCount) + ", R" + str(self.registerCount - 1) + ", R" + str(self.registerCount)
        else:
            return self.Factor(expression)

    def Factor(self, expression):
        if expression.startswith('('):
            expr = expression[1:-1]
            return self.Expr(expr)
        else:
            return expression

translator = AssemblyTranslator()
assemblyCode = translator.translate("5 + 3")
print(assemblyCode)  # Resultado: ADD R1, 5, 3
