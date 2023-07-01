from tkinter import messagebox


class NavbarController:
    def __init__(self):
        self.customer_controller = None
        self.product_controller = None

    def set_customer_controller(self, customer_controller):
        self.customer_controller = customer_controller

    def set_product_controller(self, product_controller):
        self.product_controller = product_controller
