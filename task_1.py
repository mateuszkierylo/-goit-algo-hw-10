from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Define the problem
problem = LpProblem("Maximize_Beverage_Production", LpMaximize)

# Define the decision variables
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Define the objective function
problem += lemonade + fruit_juice, "Total_Beverages"

# Define the constraints
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
problem.solve()

# Extract and print the results
optimal_lemonade = lemonade.varValue
optimal_fruit_juice = fruit_juice.varValue
max_total_products = optimal_lemonade + optimal_fruit_juice

print(f"Optimal number of Lemonade units to produce: {optimal_lemonade}")
print(f"Optimal number of Fruit Juice units to produce: {optimal_fruit_juice}")
print(f"Maximum total number of products: {max_total_products}")
