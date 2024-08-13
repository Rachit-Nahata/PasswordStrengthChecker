import tkinter as tk
import re
import hashlib

# Function to calculate password strength level
def calculate_strength(password):
    levels = {
        'Very Weak': (0, 1),
        'Weak': (2, 4),
        'Moderate': (5, 7),
        'Strong': (8, 10),
        'Very Strong': (11, float('inf'))
    }

    score = 0
    if len(password) >= 12:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*()_+]", password):
        score += 1

    for level, (min_score, max_score) in levels.items():
        if min_score <= score <= max_score:
            return level

    return 'Very Weak'

# Function to calculate crack time
def calculate_crack_time(password):
    attack_speed = 1e9
    
    char_sets = {
        'lowercase': 26,
        'uppercase': 26,
        'digits': 10,
        'special': 32
    }
    
    complexity = 0
    if re.search("[a-z]", password):
        complexity += char_sets['lowercase']
    if re.search("[A-Z]", password):
        complexity += char_sets['uppercase']
    if re.search("[0-9]", password):
        complexity += char_sets['digits']
    if re.search("[!@#$%^&*()_+]", password):
        complexity += char_sets['special']
    
    num_combinations = complexity ** len(password)
    
    time_seconds = num_combinations / attack_speed
    
    if time_seconds < 60:
        return f"{time_seconds:.2f} seconds"
    elif time_seconds < 3600:
        return f"{time_seconds / 60:.2f} minutes"
    elif time_seconds < 86400:
        return f"{time_seconds / 3600:.2f} hours"
    else:
        return f"{time_seconds / 86400:.2f} days"

# Function to check password and provide suggestions
def check_password():
    password = password_entry.get()
    
    strength = calculate_strength(password)
    
    # Suggest improvements based on password strength
    suggestions = []
    if strength == 'Very Weak':
        suggestions.append("Password is too short. Consider using at least 12 characters.")
        suggestions.append("Include uppercase letters, numbers, and special characters.")
    elif strength == 'Weak':
        suggestions.append("Consider adding uppercase letters, numbers, and special characters.")
    elif strength == 'Moderate':
        suggestions.append("Add more variety in characters (e.g., special characters).")
    
    crack_time = calculate_crack_time(password)
    
    strength_label.config(text=f"Password Strength: {strength}")
    crack_time_label.config(text=f"Estimated Crack Time: {crack_time}")
    suggestions_label.config(text="Suggestions:\n" + "\n".join(suggestions))

# Function to toggle password visibility
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

# Define styles
root.config(bg='#e0f7fa')
header_font = ('Arial', 16, 'bold')
label_font = ('Arial', 12)
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')

# Header
header_label = tk.Label(root, text="Password Strength Checker", font=header_font, bg='#b2ebf2', fg='#00796b')
header_label.pack(pady=15)

# Input field
tk.Label(root, text="Enter Password:", font=label_font, bg='#e0f7fa', fg='#00796b').pack(padx=10, pady=5)
password_entry = tk.Entry(root, width=40, font=entry_font, show="*")
password_entry.pack(padx=10, pady=5)

# Show password checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, onvalue=True, offvalue=False, command=toggle_password_visibility, bg='#e0f7fa', fg='#00796b')
show_password_checkbox.pack(padx=10, pady=5)

# Check password button
tk.Button(root, text="Check Password", font=button_font, command=check_password, bg='#00796b', fg='#ffffff').pack(padx=10, pady=10)

# Results labels
strength_label = tk.Label(root, text="Password Strength: ", font=label_font, bg='#e0f7fa', fg='#00796b')
strength_label.pack(padx=10, pady=5)

crack_time_label = tk.Label(root, text="Estimated Crack Time: ", font=label_font, bg='#e0f7fa', fg='#00796b')
crack_time_label.pack(padx=10, pady=5)

suggestions_label = tk.Label(root, text="Suggestions: ", font=label_font, bg='#e0f7fa', fg='#00796b', justify=tk.LEFT)
suggestions_label.pack(padx=10, pady=5)

# Attribution
attribution_label = tk.Label(root, text="Developed by Rachit Nahata", font=('Arial', 10), bg='#e0f7fa', fg='#00796b')
attribution_label.pack(pady=10)

root.mainloop()
