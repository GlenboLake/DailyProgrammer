from collections import defaultdict

from ply import yacc, lex
from sympy import Matrix
from sympy import lcm


# Classes that represent and balance the equation
class Reactant(object):

    def __init__(self, elements, coefficient=1):
        self.elements = elements
        self.coefficient = coefficient

    def count(self, key=None):
        if key:
            return self.count()[key]
        total = defaultdict(int)
        for element, number in self.elements:
            total[element] += number * self.coefficient
        return total

    def __str__(self):
        s = str(self.coefficient) if self.coefficient > 1 else ''
        for element in self.elements:
            s += element[0]
            if element[1] > 1:
                s += str(element[1])
        return s


class Equation(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def balance(self):
        # Get list of unique elements
        elements = set()
        [elements.add(element)
         for reactant in self.left for element in reactant.count().keys()]
        elements = tuple(elements)
        # Build the matrix
        rows = []
        for element in elements:
            row = []
            for reactant in self.left:
                row.append(reactant.count(element))
            for reactant in self.right:
                row.append(-reactant.count(element))
            rows.append(row)
        # Balance equation with linear algebra
        # http://www.ctroms.com/blog/math/2011/05/01/balancing-chemical-equations-with-linear-algebra/
        mat = Matrix(rows)
        solution, pivots = mat.rref()
        values = [solution.row(r)[-1] for r in range(solution.rows)]
        factor = lcm([value.as_numer_denom()[1] for value in values])
        coeffs = [-solution.row(i)[i] * solution.row(i)[-1]
                  * factor for i in pivots] + [factor]
        for reactant, coeff in zip(self.left + self.right, coeffs):
            reactant.coefficient = coeff
        return self

    def __str__(self):
        return '{} -> {}'.format(
            ' + '.join(map(str, self.left)),
            ' + '.join(map(str, self.right)))

# Lex/Yacc to deal with input
# Define tokens
tokens = ('NUMBER', 'SYMBOL', 'PLUS', 'YIELDS')

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Bad value! Defaulting to 1')
        t.value = 0
    return t
t_SYMBOL = r'[A-Z][a-z]?'
t_PLUS = r'\+'
t_YIELDS = r'->'
t_ignore = ' '

def t_error(t):
    print('Illegal character:', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Parser rules
def p_equation(p):
    """
    equation : side YIELDS side
    """
    p[0] = Equation(p[1], p[3])

def p_equation_half(p):
    """
    side : side PLUS reactant
    side : reactant
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_reactant(p):
    """
    reactant : NUMBER compound
    reactant : compound
    """
    if len(p) == 2:
        p[0] = Reactant(p[1])
    elif len(p) == 3:
        p[0] = Reactant(p[2], p[1])

def p_compound(p):
    """
    compound : compound species
    compound : species
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_single_species(p):
    """
    species : SYMBOL NUMBER
    species : SYMBOL
    """
    if len(p) == 2:
        p[0] = (p[1], 1)
    elif len(p) == 3:
        p[0] = (p[1], p[2])

parser = yacc.yacc()

def solve(equation):
    print(parser.parse(equation).balance())

for equation in ['Al + Fe2O4 -> Fe + Al2O3',
                 'C5H12 + O2 -> CO2 + H2O',
                 'Zn + HCl -> ZnCl2 + H2',
                 'FeCl3 + NH4OH -> FeO3H3 + NH4Cl']:
    solve(equation)
