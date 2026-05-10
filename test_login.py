from pages.cart_page import CartPage
from pages.login_page import LoginPage
from selenium import webdriver
import pytest


@pytest.mark.smoke    
def test_login(setup):

    driver = setup
    
    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert login.is_login_successful()
    
    print("Login test passed ✅")
    
    cart = CartPage(driver)

    cart.add_first_product()
    cart.add_second_product()

    cart.open_cart()
    assert cart.get_cart_items_count() == 2

    cart.remove_product()
    assert cart.get_cart_items_count() == 1
    
    
    driver.quit()    

def test_invalid_login(setup):

    driver = setup

    login = LoginPage(driver)

    login.enter_username("wrong_user")
    login.enter_password("wrong_password")
    login.click_login()
    
    assert login.is_login_failed()
    
    driver.save_screenshot("invalid_login.png")
    
    driver.quit()
   
    
