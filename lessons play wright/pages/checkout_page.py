from base_page import BasePage


class CheckOutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '#btn_action checkout_button'  # btn_action checkout_button
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = "//input[@id='postal-code']"

    def __init__(self, page):
        super().__init__(page)
        self.endpoint = '/checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_isvisible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_fields(self, first_name, last_name, postal_code, delay):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, delay=delay)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, delay=delay)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, delay=delay)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)