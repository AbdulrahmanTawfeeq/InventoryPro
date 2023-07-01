from modules.product.model.product_model import ProductModel


class ProductController:
    def add_product(self, name, price, description, customer_id):
        product = ProductModel(name=name, price=price, description=description, customer_id=customer_id)
        product.save()

    def get_all_products(self):
        return ProductModel.get_all()

    def get_product_by_id(self, product_id):
        return ProductModel.get_by_id(product_id)

    def update_product(self, product_id, name, price, description, customer_id):
        product = self.get_product_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            product.description = description
            product.customer_id = customer_id
            product.update()

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            product.delete()
