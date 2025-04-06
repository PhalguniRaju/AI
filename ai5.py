import random

def objective_function(x):
    return x+3

def hill_climb(start, step_size=0.1, max_iterations=100):
    current_x = start
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        neighbor = current_x + random.choice([-step_size, step_size])
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value:
            current_x, current_value = neighbor, neighbor_value
        else:
            break

    return current_x, current_value

start_x = random.uniform(0, 5)
best_x, best_value = hill_climb(start_x)

print(f'Best x: {best_x: .4f}, Best value: {best_value: .4f}')
