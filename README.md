# Lab: Stacks and Queues  
**Lab GitHub Repo**: [Stacks and Queues](https://github.com/learn-co-curriculum/stacks-and-queues-lab)

---

## Overview
In this lab, you’ll apply **stacks** and **queues** to solve two real-world challenges. First, you’ll implement a **parentheses validator** using a stack—a feature commonly used in compilers or formatting tools. Then, you'll simulate a **customer raffle system** using a queue, where entries are processed in the order received and a winner is selected.

By focusing on **LIFO** (last-in, first-out) and **FIFO** (first-in, first-out) behavior, you’ll develop a stronger understanding of foundational data structures used in systems like parsers, schedulers, and task processors.

---

## Task 1: Define the Problem

1. Implement a function that validates **balanced parentheses** using a stack.
2. Create a **queue** that stores customer entries and:
   - **Selects a random winner**.
   - **Dequeues up to and including** the winner.
3. Display the result of both operations clearly in your output.

**The Challenge**: Demonstrate your understanding of stack and queue behavior in common technical workflows.

---

## Task 2: Determine the Design

### Stack Functionality

- **File**: `custom_stack.py`
- **Function**:  
  - `is_valid_parentheses(s: str) -> bool`  
  - Returns `True` if the parentheses in the string are balanced.

### Queue Class Design

- **File**: `custom_queue.py`
- **Class**: `Queue`
- **Methods**:
  - `enqueue(item)`  
  - `dequeue()`  
  - `peek()`  
  - `is_empty()`  
  - `select_and_announce_winner()` → Randomly selects a winner and dequeues everyone up to and including that customer.

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.

#### Open and Run
1. Open the project in your Python-friendly IDE (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Starter code uses `pass`**:
   - You’ll see `pass` in method bodies—this is a Python placeholder.
   - Replace it with your actual code to make each method work.

2. **Build each file**:
   - Implement `Queue` methods as described above.
   - Write the stack validator function for balanced parentheses.

3. **Run Tests**:
   - Execute the provided test file with:
     ```bash
     python test_structures.py
     ```
   - Ensure all tests pass before submission.

4. **Push and Merge**:
   - Commit your work regularly.
   - Push to your feature branch.
   - Open a Pull Request (PR).
   - Merge to `main` after review.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Comment your logic**: Especially around recursive or loop-based behavior.
- **Explain your thinking** in your function definitions.
- **README**: Make sure your repo’s README includes how to run the project.
- **Clean Up**:
  - Remove debug prints.
  - Ensure your `.gitignore` ignores `.pyc`, `__pycache__`, etc.

### Run the completed lab

No third-party packages are required. From the project directory, run:

```bash
python test_structures.py
```

The bracket validator accepts only `()`, `{}`, and `[]` characters. An empty
string is balanced; any other character makes the input invalid. `Queue`
processes entries in first-in, first-out order. Its `peek`, `dequeue`, and
winner methods return `None` for an empty queue. Winner selection picks a
random queue position, announces that customer, and removes every entry up to
and including that position. Entries after the winner stay in the queue.

---

## Submission
Once your lab is complete and all tests are passing:

- Push your code to GitHub.
- Submit the link to your repo through **Canvas using CodeGrade**.
