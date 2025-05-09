from playwright.sync_api import expect


class BasePage:
    __base_url = "https://www.saucedemo.com/v1/"

    def __init__(self, page):
        self.page = page
        self.endpoint= ''

    def _get_url(self):
        return f"{self.__base_url}/{self.endpoint}"

    def _navigate_to_url (self):
        full_url = self._get_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, text):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    def wait_for_selector_and_type(self, selector, text, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, text, delay=delay)

    def assert_element_isvisible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_presents_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)