import tkinter as tk
from tkinter import messagebox

from config import get_app_title
from modules.customer.controller.customer_controller import CustomerController
from modules.navbar.controller.navbar_controller import NavbarController
from modules.navbar.view.navbar_view import NavbarView
from modules.product.controller.product_controller import ProductController


class App:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title(get_app_title())

        # Create the navbar/view and controller
        self.navbar_controller = NavbarController()
        self.navbar_controller.set_customer_controller(CustomerController())
        self.navbar_controller.set_product_controller(ProductController())

        self.navbar_view = NavbarView(self.window, self.navbar_controller)

    def run(self):
        # Run the main event loop
        self.window.mainloop()
