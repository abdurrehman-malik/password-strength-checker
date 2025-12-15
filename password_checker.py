# password_checker_gui.py
# GUI Password Strength Checker using tkinter
# Python 3.10+

import tkinter as tk
from tkinter import ttk

MAX_SCORE = 6  # maximum possible score


def evaluate_password(password: str) -> dict:
    """
    Evaluate password strength based on:
    - length
    - lowercase letters
    - uppercase letters
    - digits
    - special characters
    - common password list

    Returns a dictionary:
        {
            "score": int (0..MAX_SCORE),
            "strength": str,
            "suggestions": list[str]
        }
    """
    score = 0
    suggestions = []

    # Handle empty password
    if not password:
        return {
            "score": 0,
            "strength": "Very Weak",
            "suggestions": ["Password cannot be empty."]
        }

    # 1) Length check
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters (12+ is better).")

    # 2) Lowercase letter check
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # 3) Uppercase letter check
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # 4) Digit check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one digit (0-9).")

    # 5) Special character check
    special_chars = '!@#$%^&*()-_=+[]{};:\'",.<>?/\\|`~'
    if any(c in special_chars for c in password):
        score += 1
    else:
        suggestions.append(
            "Add at least one special character (e.g. !, @, #, ?, %, &)."
        )

    # 6) Common password check (small example list)
    common_passwords = {
        "password",
        "123456",
        "12345678",
        "123456789",
        "qwerty",
        "111111",
        "abc123",
        "iloveyou",
        "admin",
        "welcome",
    }
    if password.lower() in common_passwords:
        # Strongly penalize very common passwords
        score = 1
        suggestions.append(
            "This password is very common and easy to guess. "
            "Choose something more unique."
        )

    # Map numeric score to a strength label
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Medium"
    elif score == 5:
        strength = "Strong"
    else:  # score == 6
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "suggestions": suggestions,
    }


def check_password():
    """Callback for the 'Check Strength' button."""
    password = password_entry.get()
    result = evaluate_password(password)

    # Update strength label text
    strength_text = f"{result['strength']} (score: {result['score']}/{MAX_SCORE})"
    strength_value_label.config(text=strength_text)

    # Color based on strength
    color_map = {
        "Very Weak": "red",
        "Weak": "orangered",
        "Medium": "orange",
        "Strong": "green",
        "Very Strong": "darkgreen",
    }
    strength_value_label.config(
        fg=color_map.get(result["strength"], "black")
    )

    # Update progress bar
    strength_bar["value"] = result["score"]

    # Update suggestions area
    if result["suggestions"]:
        text = "Suggestions:\n" + "\n".join(f"• {s}" for s in result["suggestions"])
    else:
        text = "Your password satisfies all basic checks."
    suggestions_label.config(text=text)


def toggle_show_password():
    """Show/hide password characters."""
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# ----------------- GUI SETUP -----------------

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("520x320")
root.resizable(False, False)

# Main frame
main_frame = tk.Frame(root, padx=15, pady=15)
main_frame.pack(fill="both", expand=True)

# Title
title_label = tk.Label(
    main_frame,
    text="Password Strength Checker",
    font=("Arial", 16, "bold")
)
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Password label and entry
password_label = tk.Label(main_frame, text="Enter password:")
password_label.grid(row=1, column=0, sticky="e", pady=5)

password_entry = tk.Entry(main_frame, width=35, show="*")
password_entry.grid(row=1, column=1, pady=5, sticky="w")

# Show password checkbox
show_var = tk.BooleanVar(value=False)
show_checkbox = tk.Checkbutton(
    main_frame,
    text="Show password",
    variable=show_var,
    command=toggle_show_password
)
show_checkbox.grid(row=1, column=2, sticky="w", padx=(5, 0))

# Check button
check_button = tk.Button(
    main_frame,
    text="Check Strength",
    command=check_password
)
check_button.grid(row=2, column=1, pady=10, sticky="w")

# Strength label
strength_label = tk.Label(main_frame, text="Strength:")
strength_label.grid(row=3, column=0, sticky="e", pady=5)

strength_value_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 11, "bold")
)
strength_value_label.grid(row=3, column=1, sticky="w", pady=5)

# Progress bar
strength_bar = ttk.Progressbar(
    main_frame,
    length=250,
    maximum=MAX_SCORE,
    mode="determinate"
)
strength_bar.grid(row=4, column=0, columnspan=3, pady=(5, 10))

# Suggestions label (multi-line)
suggestions_label = tk.Label(
    main_frame,
    text="",
    justify="left",
    anchor="nw",
    wraplength=480
)
suggestions_label.grid(row=5, column=0, columnspan=3, sticky="w")

# Give some initial hint text
suggestions_label.config(
    text="Enter a password above and click 'Check Strength' to see the result."
)

# Start GUI event loop
root.mainloop()