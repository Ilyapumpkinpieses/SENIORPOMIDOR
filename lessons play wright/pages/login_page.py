from base_page import BasePage

class LoginPage(BasePage):
     def __init__(self, page):
         super().__init__(page)
         self.page = page
         self.endpoint = ''

     USERNAME_SELECTOR = '#user-name'
     PASSWORD_SELECTOR = '#password'
     LOGIN_BUTTON_SELECTOR = '#login-button'
     LOGOUT_BURGER = '.bm-burger-button'
     LOGOUT_BUTTON = '#logout_sidebar_link'

     def login(self, username, password):
         self._navigate_to_url()
         self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
         self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
         self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
         self.assert_text_presents_on_page('Products')

     def logout(self):
        self.wait_for_selector_and_click(self.LOGOUT_BURGER)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON)