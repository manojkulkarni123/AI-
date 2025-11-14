import itertools

# Define logical operations
def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMPLIES(p, q):
    return (not p) or q

def EQUIV(p, q):
    return p == q

# Evaluate a logical formula given a truth assignment
def eval_formula(formula, truth_assignment):
    env = truth_assignment.copy()
    env.update({'NOT': NOT, 'AND': AND, 'OR': OR, 'IMPLIES': IMPLIES, 'EQUIV': EQUIV})

    try:
        return eval(formula, {}, env)
    except Exception as e:
        print(f"Error evaluating formula '{formula}': {e}")
        return False

# Generate all possible truth assignments
def generate_truth_assignments(variables):
    for values in itertools.product([False, True], repeat=len(variables)):
        yield dict(zip(variables, values))

# Truth-table entailment check
def entails(premises, conclusion, variables):
    for assignment in generate_truth_assignments(variables):
        all_premises_true = all(eval_formula(p, assignment) for p in premises)
        conclusion_true = eval_formula(conclusion, assignment)
        if all_premises_true and not conclusion_true:
            print(f"Counterexample found: {assignment}")
            return False
    return True

# Take user input safely
def get_user_input():
    variables_input = input("Enter the list of propositional variables (comma-separated): ")
    variables = [v.strip() for v in variables_input.split(',')]

    premises = []
    n = int(input("Enter the number of premises: "))
    for i in range(n):
        premises.append(input(f"Enter premise {i+1}: ").strip())

    conclusion = input("Enter the conclusion formula: ").strip()

    return premises, conclusion, variables

# Main program
if __name__ == "__main__":
    premises, conclusion, variables = get_user_input()

    result = entails(premises, conclusion, variables)
    print(f"\nDoes the set of premises entail the conclusion? {result}")
