import tkinter as tk
from tkinter import ttk

from utils.window_utils import clear_window_content


class CustomerView:
    def __init__(self, main_window, controller):
        self.controller = controller
        self.main_window = main_window

    def display(self):
        # Remove previous content except for the menu
        clear_window_content(self.main_window)

        # Create a new window for displaying the customers table
        self.main_window.title("View Customers")

        # Create a Treeview widget
        treeview = ttk.Treeview(self.main_window)
        treeview["columns"] = ("name", "email", "phone")
        treeview.heading("name", text="Name")
        treeview.heading("email", text="Email")
        treeview.heading("phone", text="Phone")

        # Insert customers into the Treeview
        for customer in self.controller.get_all_customers():
            treeview.insert("", tk.END, values=(customer.name, customer.email, customer.phone))

        # Pack the Treeview widget
        treeview.pack(fill="both", expand=True)
