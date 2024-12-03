
products_list = [
    {'id': 1, 'name': 'Producto 1', 'price': 100, 'description': 'Descripción del producto 1', 'image': 'product1.jpg'},
    {'id': 2, 'name': 'Producto 2', 'price': 200, 'description': 'Descripción del producto 2', 'image': 'product2.jpg'},
    {'id': 3, 'name': 'Producto 3', 'price': 300, 'description': 'Descripción del producto 3', 'image': 'product3.jpg'},
]


def get_products():
    return products_list


def get_product_by_id(product_id):
    for product in products_list:
        if product['id'] == product_id:
            return product
    return None
