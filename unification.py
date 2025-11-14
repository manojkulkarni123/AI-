import re

# ----------------------------
# Helper: Parse a predicate like P(a,b)
# ----------------------------
def parse_predicate(expr):
    match = re.match(r"(\w+)\((.*)\)", expr)
    if not match:
        return expr, []  # It's just a variable or constant
    pred = match.group(1)
    args = [a.strip() for a in match.group(2).split(',')]
    return pred, args


# ----------------------------
# Unification Algorithm
# ----------------------------
def unify(x, y, substitutions=None):
    if substitutions is None:
        substitutions = {}

    # Apply existing substitutions to x and y
    x = substitute(x, substitutions)
    y = substitute(y, substitutions)

    # Case 1: identical terms
    if x == y:
        return substitutions

    # Case 2: x is a variable
    if is_variable(x):
        return unify_var(x, y, substitutions)

    # Case 3: y is a variable
    if is_variable(y):
        return unify_var(y, x, substitutions)

    # Case 4: both are compound terms (predicates)
    x_pred, x_args = parse_predicate(x)
    y_pred, y_args = parse_predicate(y)

    if x_pred != y_pred or len(x_args) != len(y_args):
        return None  # different functors or argument counts

    for a, b in zip(x_args, y_args):
        substitutions = unify(a, b, substitutions)
        if substitutions is None:
            return None

    return substitutions


# ----------------------------
# Unify variable helper
# ----------------------------
def unify_var(var, x, substitutions):
    if var in substitutions:
        return unify(substitutions[var], x, substitutions)
    elif x in substitutions:
        return unify(var, substitutions[x], substitutions)
    elif occurs_check(var, x, substitutions):
        return None  # prevent infinite loops (e.g. x = f(x))
    else:
        substitutions[var] = x
        return substitutions


# ----------------------------
# Substitute variables using current substitutions
# ----------------------------
def substitute(expr, substitutions):
    for var, val in substitutions.items():
        expr = expr.replace(var, val)
    return expr


# ----------------------------
# Occurs check (to prevent x = f(x))
# ----------------------------
def occurs_check(var, expr, substitutions):
    if var == expr:
        return True
    pred, args = parse_predicate(expr)
    for arg in args:
        if occurs_check(var, arg, substitutions):
            return True
    return False


# ----------------------------
# Variable check (lowercase = variable)
# ----------------------------
def is_variable(term):
    return isinstance(term, str) and term[0].islower()


# ----------------------------
# Demo / User Input
# ----------------------------
if __name__ == "__main__":
    print("Enter first expression (e.g. Parent(x, John)):")
    x = input("x = ").strip()
    print("Enter second expression (e.g. Parent(Mary, y)):")
    y = input("y = ").strip()

    print("\n--- Unification ---")
    result = unify(x, y)
    if result is None:
        print("❌ Unification failed.")
    else:
        print("✅ Unification successful.")
        print("Most General Unifier (MGU):", result)

"""
Enter first expression (e.g. Parent(x, John)):
x = Parent(x, John)
Enter second expression (e.g. Parent(Mary, y)):
y = Parent(Mary, y)

--- Unification ---
✅ Unification successful.
Most General Unifier (MGU): {'x': 'Mary', 'y': 'John'}
"""
