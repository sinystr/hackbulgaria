class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace, self.RAM = diskspace, RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size, self.mega_pixels = display_size, mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.income = 0

    # helps us to find if we have added the product before
    def _exists_in_store_(self, product):
        for key in self.products:
            if key == product:
                return True
        return False

    def _store_has_it_(self, product):
        if self._exists_in_store_(product) and self.products[product] > 0:
            return True
        return False

    def _execute_sell_(self, product):
        self.income += product.profit()
        self.products[product] -= 1

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            if self._exists_in_store_(product):
                self.products[product] += count
            else:
                self.products[product] = count

    def list_products(self, type_product):
        for key in self.products:
            if isinstance(key, type_product):
                print("{} - {}".format(key.name, self.products[key]))

    def total_income(self):
        print(self.income)

    def sell_product(self, product):
        if self._store_has_it_(product):
            self._execute_sell_(product)
            return True
        return False

