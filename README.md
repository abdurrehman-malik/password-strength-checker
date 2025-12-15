# Password Strength Checker (Python, CLI + GUI)

A Python-based **Password Strength Checker** that analyzes how strong a password is using simple security rules and provides suggestions to improve it.

This project includes:

- A **Command-Line Interface (CLI)** version.
- A **Graphical User Interface (GUI)** version using **tkinter**.

It is designed for **beginners** and is suitable as a **university semester project** in the field of **Cyber Security / Information Security**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Version](#cli-version)
  - [GUI Version](#gui-version)
- [How It Works (Algorithm)](#how-it-works-algorithm)
- [Examples](#examples)
- [Screenshots](#screenshots)
- [For Academic Use](#for-academic-use)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Author](#author)

---

## Overview

Passwords are the most common method for user authentication. Many users still choose weak passwords such as `123456` or `password`, which are easy to hack using brute-force or dictionary attacks.

This project aims to:

- Help users **understand** whether their password is weak or strong.
- Provide **clear suggestions** to create better passwords.
- Demonstrate basic **cybersecurity concepts** in a simple and visual way.

The tool does **not** store any passwords and works completely offline.

---

## Features

- ✅ Checks the password for:
  - Minimum **length** (8+ characters recommended)
  - Presence of **lowercase letters** (a–z)
  - Presence of **uppercase letters** (A–Z)
  - Presence of **digits** (0–9)
  - Presence of **special characters** (e.g. `! @ # ? % &`)
  - If it belongs to a small list of **very common passwords**
- ✅ Calculates a **score** (0–6)
- ✅ Assigns a **strength label**:
  - Very Weak, Weak, Medium, Strong, Very Strong
- ✅ Provides **suggestions** to improve weak passwords
- ✅ GUI features (tkinter):
  - Simple, clean window
  - "Show password" checkbox
  - Strength label with **color coding**
  - **Progress bar** representing the score
  - Multi-line suggestions area

---

## Technologies Used

- **Programming Language:** Python 3.10+
- **Libraries:**
  - `tkinter` and `tkinter.ttk` for GUI (built-in Python standard library)
- **Tools (optional):**
  - Any code editor: VS Code, PyCharm, IDLE, etc.

No third-party packages are required. No `pip install` is needed.

---

## Project Structure

```text
password-strength-checker/
├─ password_checker.py        # Command-line version (CLI)
├─ password_checker_gui.py    # Graphical version (GUI with tkinter)
├─ README.md                  # Project documentation (this file)
├─ LICENSE                    # MIT License
├─ requirements.txt           # Basic environment info (Python version)
└─ .gitignore                 # Ignore Python cache, virtualenvs, etc.
