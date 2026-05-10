class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
        self.driver.find_element(
            "xpath",
            "(//button[starts-with(@id,'add-to-cart')])[1]"
        ).click()

    def add_second_product(self):
        self.driver.find_element(
            "xpath",
            "(//button[starts-with(@id,'add-to-cart')])[2]"
        ).click()

    def open_cart(self):
        self.driver.find_element(
            "class name",
            "shopping_cart_link"
        ).click()

    def remove_product(self):
        self.driver.find_element(
            "xpath",
            "(//button[starts-with(@id,'remove')])[1]"
        ).click()
        
    def get_cart_items_count(self):

        items = self.driver.find_elements(
        "class name",
        "inventory_item_name"
    )

        return len(items)