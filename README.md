# Stack-Based Recursion Simulation

## Description
This Python script demonstrates how recursive functions can be simulated using an iterative approach with a manually implemented dynamic `Stack` class. It compares recursive and stack-based solutions across a variety of mathematical and traversal problems, and logs all results to an output file.

## Purpose
To explore and understand how recursion can be transformed into iteration using a stack, and to compare the output and behavior of both approaches.

## Files
- `main.py` – Contains all class definitions, function implementations, and the logic to write output to file.
- `stack_output.txt` – The output file that stores results for each test case, comparing recursive and iterative outputs.

## Components

### Stack Class
A dynamic array-based stack implementation that:
- Starts with a fixed size of 10.
- Automatically doubles in size when full.
- Supports standard operations: `push`, `pop`, `peak`, `isEmpty`, `isFull`.

### Functions Implemented

#### Function 1 – Collatz-like Sequence
- `F_1(n)`: Recursive version that builds a list by applying the Collatz rule.
- `function_1(n)`: Iterative version that simulates the recursive behavior using a stack.

#### Function 2 – Recursive Branching Pattern
- `F_2(n)`: Recursively divides `n` into smaller branches if `n >= 6`.
- `function_2(n)`: Iterative version using a stack to simulate recursive control flow.

#### Function 3 – In-Order Binary Traversal
- `F_3(a, b)`: Performs in-order traversal of a conceptual binary tree using midpoint logic.
- `function_3(a, b)`: Iterative version that simulates the traversal using a stack.

#### Function 4 – Post-Order Binary Traversal
- `F_4(a, b)`: Similar to Function 3, but appends the midpoint after visiting both child intervals.
- `function_4(a, b)`: Iterative version that maintains post-order traversal behavior.

## How to Run

1. Ensure you have Python 3 installed.
2. Run the script:

