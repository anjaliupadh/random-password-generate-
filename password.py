import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg='#d3d3d3')  # Light gray background

        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg='#d3d3d3', fg='blue')
        self.title_label.pack(pady=20)

        # Password Length
        self.length_label = tk.Label(root, text="Password Length:", font=("Arial", 12), bg='#d3d3d3', fg='black')
        self.length_label.pack()
        self.length_spinbox = ttk.Spinbox(root, from_=8, to_=32, width=5, font=("Arial", 12))
        self.length_spinbox.pack(pady=5)

        # Complexity Options
        self.include_uppercase = tk.BooleanVar()
        self.include_uppercase.set(True)
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase, font=("Arial", 12), bg='#d3d3d3', fg='black', selectcolor='#d3d3d3')
        self.uppercase_check.pack()

        self.include_numbers = tk.BooleanVar()
        self.include_numbers.set(True)
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers, font=("Arial", 12), bg='#d3d3d3', fg='black', selectcolor='#d3d3d3')
        self.numbers_check.pack()

        self.include_symbols = tk.BooleanVar()
        self.include_symbols.set(True)
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols, font=("Arial", 12), bg='#d3d3d3', fg='black', selectcolor='#d3d3d3')
        self.symbols_check.pack()

        # Generate Button
        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password, style='TButton')
        self.generate_button.pack(pady=15)

        # Password Entry
        self.password_entry = tk.Entry(root, width=30, font=("Arial", 14), justify="center", bg='white', fg='black')
        self.password_entry.pack(pady=10)

        # Copy Button
        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, style='TButton')
        self.copy_button.pack()

        # Style configuration
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12, 'bold'), background='blue', foreground='black')
        style.map('TButton', background=[('active', 'blue')])

    def generate_password(self):
        length = int(self.length_spinbox.get())
        chars = string.ascii_lowercase
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_numbers.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation

        if length < 8:
            messagebox.showwarning("Weak Password", "Password length should be at least 8 characters.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Empty", "Generate a password first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

