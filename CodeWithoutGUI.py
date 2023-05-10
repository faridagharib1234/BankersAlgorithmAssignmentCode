def is_safe(num_processes, num_resources, available, max_resources, allocated, process_id, request):
    # Calculate the need matrix
    need = [[max_resources[i][j] - allocated[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # Check if the request is valid
    for j in range(num_resources):
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
    for j in range(num_resources):
        temp_available[j] -= request[j]
        temp_allocated[process_id][j] += request[j]
        temp_need[process_id][j] -= request[j]

    # Initialize the finish matrix to false for all processes
    finish = [False] * num_processes

    # Try to find a safe sequence using a modified version of the Banker's algorithm
    work = temp_available.copy()
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(temp_need[i][j] <= work[j] for j in range(num_resources)):
                finish[i] = True
                work = [work[j] + temp_allocated[i][j] for j in range(num_resources)]
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
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))
    available = [int(x) for x in input("Enter total resources: ").split()]
    allocated = []
    max_resources = []
    for i in range(num_processes):
        allocated.append([int(x) for x in input(f"Enter current allocation for process {i}: ").split()])
        max_resources.append([int(x) for x in input(f"Enter maximum need for process {i}: ").split()])
    process_id = int(input(f"Enter process id (0-{num_processes - 1}): "))
    request = [int(x) for x in input("Enter requested resources: ").split()]

    # Check if the request is safe or unsafe
    is_safe(num_processes, num_resources, available, max_resources, allocated, process_id, request)

except ValueError:
    print("Error: Invalid input.")
except IndexError:
    print("Error: Process ID is out of range.")
