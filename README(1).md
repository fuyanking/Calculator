# Simple In‑fix Expression Calculator
AP Computer Science Principles Create Performance Task Project

## Project Overview
This is a Python calculator program that evaluates standard infix mathematical expressions with `+`, `-`, `*`, `/` and parentheses `()`.
Users can type in math expressions like `3+4*2` or `(5‑2)*8`, and the program computes the correct result respecting operator precedence (multiplication and division before addition and subtraction).

This project was completed for the AP CSP Create Performance Task, where I designed and implemented a program to solve a real‑world problem: manually calculating long expressions with parentheses is error‑prone, so this tool automates that computation.

## Core Program Features
- Supports four basic arithmetic operations: addition `+`, subtraction `-`, multiplication `*`, division `/`
- Respects operator precedence: `*` `/` calculate before `+` `-`
- Handles parentheses `()` to change calculation order
- Supports multi‑digit integers
- Interactive loop: users can compute multiple expressions until they choose to exit
- Input validation for continue‑or‑quit command

## How It Works (Algorithm Idea)
The program uses **two stacks (lists in Python)** to parse and compute expressions:
1. `num_stack`: stores numeric values
2. `op_stack`: stores operators and parenthesis symbols

Key logic:
1. Iterate character‑by‑character through the user input string.
2. Collect consecutive digits to form multi‑digit numbers and push numbers onto the number stack.
3. When encountering an operator or parenthesis: compare operator priority. Higher‑priority operations get calculated first by popping values from stacks.
4. For parentheses: compute inside the parenthesis pair before moving outward.
5. After finishing reading the whole input expression, finish remaining operations left in the stacks.
6. Return the final computed answer.

> Stack is a LIFO (Last‑In‑First‑Out) structure. Special care is taken for subtraction and division: the pop‑order of numbers matters to avoid wrong calculation results.

## How to Run
### Requirements
- Python 3.11 or newer Python 3 version installed. No external libraries needed.

### Steps
1. Download `calculator_ver4.py` file to your local machine
2. Open terminal / command prompt, navigate to the file folder
3. Run command:
```bash
python calculator_ver4.py
