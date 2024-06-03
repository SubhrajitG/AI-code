def hill_climbing(function, start_point, step_size, max_iterations):
    current_point = start_point
    current_value = function(current_point)

    for iteration in range(max_iterations):
        next_point = current_point + step_size
        next_value = function(next_point)
        
        if next_value > current_value:
            current_point = next_point
            current_value = next_value
        else:
            next_point = current_point - step_size
            next_value = function(next_point)
            
            if next_value > current_value:
                current_point = next_point
                current_value = next_value
            else:
                break

        print("Iteration {iteration + 1}: Point = {current_point}, Value = {current_value}")

    return current_point, current_value

# Get user input for the function, starting point, step size, and max iterations
user_function = input("Enter the function to be optimized (use 'x' as the variable): ")

# Define the function to be optimized
def function(x):
    return eval(user_function)

# Get the starting point, step size, and max iterations from the user
start_point = float(input("Enter the starting point: "))
step_size = float(input("Enter the step size: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Perform hill climbing
best_point, best_value = hill_climbing(function, start_point, step_size, max_iterations)

print(f"\nBest point found: {best_point}")
print(f"Value at best point: {best_value}")
