# BankersAlgorithmAssignmentCode

This program implements the Banker's algorithm, which is a resource allocation and deadlock avoidance algorithm used in operating systems.

## How to Use

1. Run the `main.py` file.
2. Enter the number of processes and resources when prompted.
3. Enter the maximum resource allocation for each process when prompted.
4. Enter the current resource allocation for each process when prompted.
5. The program will output whether the system is in a safe state or not.

## Dependencies

This program requires the `tkinter` module to be installed.

## Input Requirements

The number of processes and resources must be positive integers.
The maximum resource need and allocated resources must be non-negative integers.
The number of resources allocated to a process must not exceed the maximum resource need for that process.

## Output
The program will output whether the system is in a safe state or not. If the system is in a safe state, the program will also output the safe sequence of processes.

## Files

- `CodeWithoutGUI.py`: This is the main file of the program that runs the Banker's algorithm.
- `CodeWithGUI.py`: This is the main file of the program that runs the Banker's algorithm with a GUI in it.
- `README.md`: This file contains information about the program and how to use it.

## Numbers used while running the code:

Numbers for a safe request:
Enter the number of processes: 3
Enter the number of resources: 4
Enter total resources: 6 4 7 3
Enter current allocation for process 0: 1 0 2 1
Enter current allocation for process 1: 0 1 3 0
Enter current allocation for process 2: 1 2 1 1
Enter maximum need for process 0: 4 1 3 2
Enter maximum need for process 1: 1 3 5 1
Enter maximum need for process 2: 3 3 3 3
Enter process id (0-2): 1
Enter requested resources: 0 1 1 0
The request is safe.

Numbers used for an unsafe request:
Enter the number of processes: 5
Enter the number of resources: 3
Enter total resources: 10 10 10
Enter current allocation for process 0: 0 1 0
Enter current allocation for process 1: 3 0 2
Enter current allocation for process 2: 3 0 2
Enter current allocation for process 3: 2 1 1
Enter current allocation for process 4: 0 0 2
Enter maximum need for process 0: 7 5 3
Enter maximum need for process 1: 5 2 5
Enter maximum need for process 2: 9 0 2
Enter maximum need for process 3: 2 3 3
Enter maximum need for process 4: 4 3 3
Enter process id (0-4): 2
Enter requested resources: 2 0 1
The request is unsafe

## Screenshots while the code is running!

First, while it gives me that the request is safe:
![1](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/fbcf578f-21bb-49e8-a307-eee55472c1e6)
![2](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/026c01c9-461c-4be5-9785-2d57b97acdd1)

Second, while it gives me that the request is unsafe:
![3](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/97318b45-9a66-4139-8b5a-8f32ec6f8171)
![4](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/81d999af-6a4f-4eb6-9148-b50abd337eae)

## Author

This program was created by [Farida Abdel Baky].
