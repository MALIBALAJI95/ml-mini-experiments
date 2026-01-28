# Day 07 – Activation Functions From Scratch

## Project Overview
This project implements and compares common activation functions used in neural
networks using pure Python.

The goal is to understand how activation functions affect learning.

---

## Objective
To analyze the behavior of Sigmoid, Tanh, and ReLU activation functions and
their derivatives.

---

## Activation Functions Implemented
- Sigmoid
- Tanh
- ReLU

---

## Why Activation Functions Matter
Activation functions:
- Introduce non-linearity
- Control gradient flow
- Decide learning speed
- Impact deep network performance

---

## Mathematical Properties

### Sigmoid
- Output range: (0, 1)
- Problem: Vanishing gradients

### Tanh
- Output range: (-1, 1)
- Zero-centered but still saturates

### ReLU
- Output range: (0, ∞)
- Fast learning
- Risk of dying neurons

---

## Implementation Details
1. Implemented activation functions
2. Implemented derivatives
3. Tested on multiple input values
4. Compared outputs and gradients

---

## Output
The script prints:
- Activation values
- Derivative values
- Comparison across inputs

---

## How to Run
```bash
python activation_functions.py
