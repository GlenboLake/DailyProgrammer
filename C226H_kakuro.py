from collections import namedtuple
from copy import copy
from itertools import product
import string


class KakuroSolver(object):
    Rule = namedtuple('Rule', ['cells', 'sum'])
    values = set(range(1, 10))

    def __init__(self, rows, cols, rules, cells=None, guess=None):
        self.rows, self.cols = rows, cols
        self.rules = rules
        if cells:
            self.cells = copy(cells)
        else:
            self.cells = {}
            # Initialize cells to have any possible digit
            for rule in self.rules:
                for cell in rule.cells:
                    self.cells[cell] = self.values
        # Apply guess
        if guess:
            self.cells[guess[0]] = set([guess[1]])
        self.unsolved_cells = [
            k for k, v in self.cells.items() if len(v) > 1]

    @classmethod
    def from_text_file(cls, filename):
        """Read a text file and create a solver based on the rules therein."""
        contents = open('input/kakuro.txt').read().splitlines()
        cols, rows = list(map(int, contents[0].split()))
        rules = []
        for line in contents[1:]:
            rowdata = line.split()
            rules.append(KakuroSolver.Rule(rowdata[1:], int(rowdata[0])))
        return cls(rows, cols, rules)

    def get_cell(self, cell_name):
        # Get the value of a cell. If it's a set of length one, just return
        # that value.
        if cell_name in self.cells:
            if len(self.cells[cell_name]) == 1:
                return list(self.cells[cell_name])[0]
            else:
                return self.cells[cell_name]
        else:
            return None

    def get_rules_for_cell(self, cell_name):
        return [rule for rule in self.rules if cell_name in rule.cells]

    def get_digits(self, rule, disallowed_values=[]):
        # For a given rule, get the digits that can go in one of the squares.
        # disallowed_values is a list of digits already populated by cells
        # affected by the rule.
        values = [val for val in self.values if val not in disallowed_values]
        count = len(rule.cells) - len(disallowed_values)
        sum_ = rule.sum - sum(disallowed_values)
        digits = set()
        for combo in product(values, repeat=count):
            if len(set(combo)) != count:
                # Only interested in unique values
                continue
            if sum(combo) == sum_:
                # Only interested in sets that add to the right sum
                digits = digits.union(combo)
                if digits == self.values:
                    break
        return digits

    def constrain(self, cell):
        # If the cell has been determined, there's no further constraint.
        if isinstance(self.get_cell(cell), int):
            return False
        rules = self.get_rules_for_cell(cell)
        values = self.values
        invalid = set()
        for rule in rules:
            invalid_for_rule = set()  # Digits already used for this rule
            other_cells = [c for c in rule.cells if c != cell]
            for other in other_cells:
                if isinstance(self.get_cell(other), int):
                    invalid_for_rule.add(self.get_cell(other))
            rule_values = self.get_digits(rule, invalid_for_rule)
            values = values.intersection(rule_values)
            invalid = invalid.union(invalid_for_rule)
        before = self.cells[cell]
        after = self.cells[cell] = before.intersection(values) - invalid
        if len(after) == 1:
            self.unsolved_cells.remove(cell)
        return before != after

    def is_solved(self):
        return len(self.unsolved_cells) == 0

    def solve(self):
        # Constrain as far as we can without guessing
        improvement_made = True
        while improvement_made and not self.is_solved():
            improvement_made = False
            for cell in self.unsolved_cells:
                improvement_made |= self.constrain(cell)
                if len(self.cells[cell]) == 0:
                    return False
        if self.is_solved():
            return True
        # Now we have to start guessing!
        for cell in self.unsolved_cells:
            # Pick an unsolved cell. For a solvable grid, this loop should
            # never hit its second iteration.
            values = self.cells[cell]
            for value in values:
                # Try each possible value and see if it produces a solution
                guess = KakuroSolver(self.rows, self.cols, self.rules, self.cells, (cell, value))
                if guess.solve():
                    # On successful solution, copy the cell data to this instance
                    self.cells = guess.cells
                    self.unsolved_cells = guess.unsolved_cells
                    return True
        return True

    def __str__(self, *args, **kwargs):
        columns = string.ascii_uppercase[:self.cols]
        # Headers
        s = '    ' + ' '.join(columns)
        s += '\n--+' + '--' * self.cols
        # Add rows, one at a time
        for row in range(1, self.rows + 1):
            s += '\n' + str(row) + ' |'
            for col in columns:
                s += ' '
                cell = self.get_cell(col + str(row))
                if cell:
                    if isinstance(cell, int):
                        # Solved cell
                        s += str(cell)
                    else:
                        # Unsolved cell
                        s += '?'
                else:
                    # Empty cell
                    s += ' '
        return s


solver = KakuroSolver.from_text_file('input/kakuro.txt')

solver.solve()
print(solver)
