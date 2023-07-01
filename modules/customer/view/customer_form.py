import tkinter as tk

from utils.form_utils import clear_form
from utils.window_utils import clear_window_content


class CustomerForm:
    def __init__(self, main_window, controller):
        self.save_button = None
        self.phone_entry = None
        self.phone_label = None
        self.email_entry = None
        self.email_label = None
        self.name_entry = None
        self.name_label = None
        self.controller = controller
        self.main_window = main_window

    def display(self):
        # Remove previous content except for the menu
        clear_window_content(self.main_window)

        # Create form elements
        self.name_label = tk.Label(self.main_window, text="Name:")
        self.name_entry = tk.Entry(self.main_window)

        self.email_label = tk.Label(self.main_window, text="Email:")
        self.email_entry = tk.Entry(self.main_window)

        self.phone_label = tk.Label(self.main_window, text="Phone:")
        self.phone_entry = tk.Entry(self.main_window)

        self.save_button = tk.Button(self.main_window, text="Save", command=self.save_customer)

        # Place form elements in the main window
        self.name_label.pack()
        self.name_entry.pack()

        self.email_label.pack()
        self.email_entry.pack()

        self.phone_label.pack()
        self.phone_entry.pack()

        self.save_button.pack()

    def save_customer(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        self.controller.add_customer(name, email, phone)

        clear_form(self)
