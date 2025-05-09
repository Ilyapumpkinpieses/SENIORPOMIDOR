from base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR='.inventory_item a:has-text("Sauce Labs Backpack")'
    SHOPPING_CART_LINK_SELECTOR= '#shopping_cart_container'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.assert_element_isvisible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)