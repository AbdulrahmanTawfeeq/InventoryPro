import tkinter as tk


class NavbarView:
    def __init__(self, window, navbar_controller):
        self.window = window
        self.product_controller = navbar_controller.product_controller
        self.customer_controller = navbar_controller.customer_controller
        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.create_menu()

    def create_menu(self):
        if self.product_controller is not None:
            products_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="Products", menu=products_menu)
            products_menu.add_command(label="Add Product", command=lambda: self.product_controller.form)
            products_menu.add_command(label="View Products", command=lambda: self.product_controller.view)

        if self.customer_controller is not None:
            customers_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="Customers", menu=customers_menu)
            customers_menu.add_command(label="Add Customer", command=lambda: self.customer_controller.form(self.window))
            customers_menu.add_command(label="View Customers", command=lambda: self.customer_controller.view(self.window))
