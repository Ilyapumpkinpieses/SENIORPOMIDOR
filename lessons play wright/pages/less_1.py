from playwright.sync_api import sync_playwright
import time

from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage

# playwright= sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=500)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
#
# page.type(selector='[id="user-name"]', text='standard_user', delay=100)
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button') #[class='submit-button']'
#
# page.wait_for_url('https://www.saucedemo.com/inventory.html',timeout=10000)
# page.wait_for_selector('#inventory_container')
#
# button_add_cart='[data-test="add-to-cart-sauce-labs-backpack"]'
# alt_locator_for_card = ".inventory_item a:has-text('Sauce Labs Backpack')"
# card_button= '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
#
# page.is_visible(selector=button_add_cart)
# page.is_enabled(selector=button_add_cart)
# #page.click(selector=button_add_cart)
# #page.click(selector=alt_locator_for_card)
# page.click(card_button)
# page.is_visible('[data-test="shopping-cart-link"]')
# page.click('[data-test="shopping-cart-link"]')
# page.wait_for_url('https://www.saucedemo.com/cart.html',timeout=10000)
# button_checkout='#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(button_checkout)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html', timeout=1000)
#
# page.fill(selector='#first-name', value='FirstName')
# page.fill(selector='#last-name', value='LastName')
# page.fill(selector='#postal-code', value='954234543')
#
# page.click('[id="continue"][type="submit"]')
# page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html')
# page.wait_for_selector('button:has text("Finish")')
# page.click('button:has text("Finish")')
# page.wait_for_url('https://www.saucedemo.com/checkout-complete.html')
#
#
# time.sleep(7)
#
# browser.close()
# playwright.stop()



def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.fill_checkout_form("John", "Doe", '12345')
