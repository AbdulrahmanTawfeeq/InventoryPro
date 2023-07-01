from modules.customer.model.customer_model import CustomerModel
from modules.customer.view.customer_form import CustomerForm
from modules.customer.view.customer_view import CustomerView


class CustomerController:
    def form(self, main_window):
        form_view = CustomerForm(main_window, self)
        form_view.display()

    def view(self, main_window):
        # Create an instance of the CustomerView class and display the customers
        customer_view = CustomerView(main_window, self)
        customer_view.display()

    def add_customer(self, name, email, phone):
        customer = CustomerModel(name=name, email=email, phone=phone)
        customer.save()

    def get_all_customers(self):
        return CustomerModel.get_all()

    def get_customer_by_id(self, customer_id):
        return CustomerModel.get_by_id(customer_id)

    def update_customer(self, customer_id, name, email, phone):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.name = name
            customer.email = email
            customer.phone = phone
            customer.update()

    def delete_customer(self, customer_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.delete()
