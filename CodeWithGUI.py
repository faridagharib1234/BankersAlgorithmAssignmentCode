import tkinter as tk
from tkinter import messagebox, simpledialog


def input_box(prompt):
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Input", prompt)
    return user_input


def display_message(message):
    messagebox.showinfo("Message", message)


def run_banker_algorithm():
    num_processes = int(input_box("Enter the number of processes: "))
    num_resources = int(input_box("Enter the number of resources: "))

    # Get available resources
    available_str = input_box("Enter the number of available resources (separated by commas): ")
    available = list(map(int, available_str.split(",")))

    # Get maximum demand of each process
    max_demand = []
    for i in range(num_processes):
        max_demand_str = input_box(f"Enter the maximum resource demand of process {i} (separated by commas): ")
        max_demand.append(list(map(int, max_demand_str.split(","))))

    # Get resources allocated to each process
    allocation = []
    for i in range(num_processes):
        allocation_str = input_box(f"Enter the resources allocated to process {i} (separated by commas): ")
        allocation.append(list(map(int, allocation_str.split(","))))

    # Calculate the need of each process
    need = []
    for i in range(num_processes):
        need.append([max_demand[i][j] - allocation[i][j] for j in range(num_resources)])

    # Initialize the finish array to false for each process
    finish = [False] * num_processes

    # Initialize the work and finish arrays to the current available resources
    work = available.copy()

    # Initialize a list to hold the safe sequence, if one exists
    safe_sequence = []

    # Run the algorithm until either a safe sequence is found or it is determined that no safe sequence exists
    while True:
        # Find an i such that both:
        # - The ith process is not finished (finish[i] == False)
        # - The ith process has a need that is less than or equal to the work for all resources (need[i][j] <= work[j])
        i = None
        for p in range(num_processes):
            if not finish[p] and all(need[p][j] <= work[j] for j in range(num_resources)):
                i = p
                break

        # If no such i exists, break out of the loop and check if all processes are finished
        if i is None:
            if all(finish):
                display_message(f"Safe sequence: {safe_sequence}")
                break
            else:
                display_message("No safe sequence exists.")
                break

        # If an i was found, add it to the safe sequence and update the work array
        safe_sequence.append(i)
        for j in range(num_resources):
            work[j] += allocation[i][j]
        finish[i] = True


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Banker's Algorithm")

    title_label = tk.Label(root, text="Banker's Algorithm", font=("Arial Bold", 16))
    title_label.pack(pady=10)

    run_button = tk.Button(root, text="Run", command=run_banker_algorithm)
    run_button.pack(pady=10)

    root.mainloop()
