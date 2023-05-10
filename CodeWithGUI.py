import tkinter as tk
from tkinter import simpledialog


def input_box(prompt):
    """
    Displays a simple dialog box for user input and returns the input as a string.
    """
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Input", prompt)
    return user_input


def is_safe(available, allocated, max_resources, process_id, request):
    """
    Determines whether allocating the requested resources to the specified process would result in a safe state.
    """
    # Calculate the need matrix
    need = [list(map(lambda x, y: x - y, max_resources[i], allocated[i])) for i in range(len(max_resources))]

    # Check if the request is valid
    for j in range(len(available)):
        if request[j] > need[process_id][j]:
            print("Error: The requested resources exceed the maximum need.")
            return False
        if request[j] > available[j]:
            print("Error: The requested resources are not available.")
            return False

    # Try to allocate the resources and update the available, allocated, and need matrices
    temp_available = available.copy()
    temp_allocated = [row[:] for row in allocated]
    temp_need = [row[:] for row in need]
    for j in range(len(available)):
        temp_available[j] -= request[j]
        temp_allocated[process_id][j] += request[j]
        temp_need[process_id][j] -= request[j]

    # Initialize the finish matrix to false for all processes
    finish = [False] * len(max_resources)

    # Try to find a safe sequence using a modified version of the Banker's algorithm
    work = temp_available.copy()
    while True:
        found = False
        for i in range(len(max_resources)):
            if not finish[i] and all(temp_need[i][j] <= work[j] for j in range(len(available))):
                finish[i] = True
                work = [work[j] + temp_allocated[i][j] for j in range(len(available))]
                found = True
                break
        if not found:
            break

    # If a safe sequence was found, the request is safe; otherwise, it's unsafe
    if all(finish):
        print("The request is safe.")
        return True
    else:
        print("The request is unsafe.")
        return False


# Get input from the user
try:
    num_processes = int(input_box("Enter the number of processes: "))
    num_resources = int(input_box("Enter the number of resources: "))
    available = [int(x) for x in input_box("Enter total resources: ").split()]
    allocated = []
    max_resources = []
    for i in range(num_processes):
        allocated.append([int(x) for x in input_box(f"Enter current allocation for process {i}: ").split()])
        max_resources.append([int(x) for x in input_box(f"Enter maximum need for process {i}: ").split()])
    process_id = int(input_box(f"Enter process id (0-{num_processes - 1}): "))
    request = [int(x) for x in input_box("Enter requested resources: ").split()]

    # Check if the request is safe or unsafe
    is_safe(available, allocated, max_resources, process_id, request)

except ValueError:
    print("Error: Invalid input.")
except IndexError:
    print("Error: Process ID is out of range.")
