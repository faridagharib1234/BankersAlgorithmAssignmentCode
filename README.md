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

## Installation
To get started with the project, simply clone the repository to your computer:
 
 ```bash
https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode.git
 ```

## Numbers used while running the code:

*Here are some numbers you can use to test if the program can detect an unsafe state:
- num_processes = 3, num_resources = 3
- available = [3, 3, 2]
- max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
- allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
-> This will result in an unsafe state, and the program should detect that no safe sequence exists.

*Here's an example input that should produce a safe state:
- num_processes = 5, num_resources = 3
- available = [3, 3, 2]
- max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
- allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
->The safe sequence for this input should be: [1, 3, 4, 0, 2]

## Screenshots while the code is running!

*Banker's Algorithm:
![1](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/d4c49f46-b919-4511-89de-5d208a269a83)

*First, while it gives me that the request is safe:
![Safe Sequence](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/78638174-72bb-428d-bf9a-ff078b308c4c)

*Second, while it gives me that the request is unsafe:
![Not safe](https://github.com/faridagharib1234/BankersAlgorithmAssignmentCode/assets/58792738/d24e0d45-c30f-449b-8295-c3ba36aba3b5)

## Author

This program was created by [Farida Abdel Baky].
