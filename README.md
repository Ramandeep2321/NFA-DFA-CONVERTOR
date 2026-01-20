# NFA-DFA-CONVERTOR
This project implements the conversion of NFA to DFA using Python. It accepts user-defined automata inputs, generates transition tables, identifies final and dead states, and ensures deterministic behavior for efficient computation. The project bridges automata theory with real-world implementation.

# NFA to DFA Conversion using Python

## Project Title
Conversion of Non-Deterministic Finite Automaton (NFA) to Deterministic Finite Automaton (DFA)

---

## Description
This project implements the conversion of a Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA) using Python. NFAs are easier to design but inefficient during execution, whereas DFAs are deterministic and faster.  
The program takes user-defined NFA inputs and generates DFA transition tables while preserving the same language.

It also identifies final states and dead states in the DFA, making the automaton more suitable for practical applications.

---

## Objectives
- Understand NFA and DFA concepts
- Convert NFA to DFA using Python
- Display transition tables
- Identify DFA final states
- Detect dead states

---

## Technologies Used
- Programming Language: Python 3.11
- IDE: PyCharm Community Edition
- Library: NumPy

---

## Features
- User input for NFA states, symbols, and transitions
- Automatic NFA to DFA conversion
- Formatted transition tables
- DFA final state detection
- Dead state identification

---

## Input
- Number of states
- Input symbols
- Start state
- Accepting states
- Transitions for each state and symbol

---

## Output
- NFA Transition Table
- DFA Transition Table
- DFA Final States
- Updated DFA Table including Dead States
- List of Dead States

---

## How to Run
1. Install Python 3.11
2. Open the project in PyCharm Community
3. Install NumPy using:
