import tkinter as tk
def deliver_data(data, text_widget):
    text_widget.insert(tk.END, f"{data}\n")