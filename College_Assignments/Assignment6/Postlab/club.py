class Product:
    def __init__(self, price, code):
        self.product_code = code
        self.product_price = price


class Store:
    def __init__(self, name):
        self.name_of_store = name
        self.code_object_dict = {}  # dict of code of the product and the object of that product
        self.code_total_price_of_that_product_dict = {}

    def creating_products(self, price, code):
        product = Product(price, code)
        self.code_object_dict.update({code: product})

    def start(self):
        print("Welcome to {} stores".format(self.name_of_store))
        # creating 5 demo products for the store
        self.creating_products(100, "xyz1")
        self.creating_products(200, "xyz2")
        self.creating_products(300, "xyz3")
        self.creating_products(400, "xyz4")
        self.creating_products(500, "xyz5")

        print("products are:")
        for key in self.code_object_dict:
            print("{} : {}".format(key, self.code_object_dict[key].product_price))

        print("Enter the quantity of each item required:")
        print("Enter zero if you dont want that item")

        for key in self.code_object_dict:
            print("For item : ", key)
            print("Enter the quantity needed")
            quantity = int(input())
            total_price_of_that_product = quantity * self.code_object_dict[key].product_price
            self.code_total_price_of_that_product_dict.update({key: total_price_of_that_product})

        sum = 0
        for key in self.code_total_price_of_that_product_dict:
            sum = sum + self.code_total_price_of_that_product_dict[key]

        for key in self.code_total_price_of_that_product_dict:
            print("Product: ", key)
            print("Total cost for product: {} including all items of this product is: {} : ".format(key,
                                                                                                    self.code_total_price_of_that_product_dict[
                                                                                                        key]))

        print("The total amount for shopping is : ", sum)


store1 = Store("Xpress")
store1.start()
