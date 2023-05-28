import numpy as np

def bankers_algorithm(available, max_demand, allocated):
    num_processes = len(allocated)
    num_resources = len(available)

    work = available.copy()
    finish = np.zeros(num_processes, dtype=bool)
    need = max_demand - allocated

    # Iterate until all processes are finished or no process can be executed
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i] <= work):
                # Process can be executed
                work += allocated[i]
                finish[i] = True
                found = True
        if not found:
            break

    # Check if all processes finished
    if all(finish):
        return True  # System is in a safe state
    else:
        return False  # System is in an unsafe state


# Example usage
available_resources = np.array([2, 1, 0])
maximum_demand = np.array([[4, 3, 3],
                           [3, 2, 2],
                           [9, 0, 2],
                           [7, 5, 3],
                           [1, 1, 2]])
allocated_resources = np.array([[1, 1, 2],
                                [2, 1, 2],
                                [4, 0, 1],
                                [0, 2, 0],
                                [1, 1, 2]])

if bankers_algorithm(available_resources, maximum_demand, allocated_resources):
    print("System is in a safe state.")
else:
    print("System is in an unsafe state.")
