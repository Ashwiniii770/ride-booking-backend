# Stack Implementation in Python

## Overview

This project demonstrates the implementation of a **Stack Data Structure in Python**.
A stack follows the **LIFO (Last In First Out)** principle, meaning the last element added to the stack is the first element removed.

Example: A stack of plates where the top plate is removed first.

## Stack Operations

The following basic operations are implemented:

* **Push** – Add an element to the stack
* **Pop** – Remove the top element from the stack
* **Peek** – View the top element of the stack
* **isEmpty** – Check whether the stack is empty

## Implementation

```python
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop element
stack.pop()
print("Stack after pop:", stack)

# Peek top element
print("Top element:", stack[-1])
```

## Example Output

```
Stack after push: [10, 20, 30]
Stack after pop: [10, 20]
Top element: 20
```

## Applications of Stack

Stacks are widely used in computer science problems such as:

* Balanced Parentheses Checking
* Expression Evaluation
* Undo/Redo Operations
* Depth First Search (DFS)
* Backtracking Algorithms

## Technologies Used

* Python

## Author

Ashwini
