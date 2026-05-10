from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element("xpath","//*[@id='user-name']").send_keys('standard_user')
driver.find_element("xpath","//*[@id='password']").send_keys('secret_sauce')
driver.find_element("xpath","//*[@id='login-button']").click()

print("login successful")

# add to cart

driver.find_element("xpath","(//button[starts-with(@id,'add-to-cart')])[1]").click()
print("first product successfully added in the cart")
driver.find_element("xpath","(//button[starts-with(@id,'add-to-cart')])[2]").click()
print("second product successfully added in the cart")

# go to cart section
driver.find_element("xpath","//*[@id='shopping_cart_container']/a").click()
print("show cart section")

# verify cart items
items = driver.find_elements("class name", "inventory_item_name")

assert len(items) == 2
print("2 items present in cart ✅")

# remove 1 item
driver.find_element("xpath", "(//button[starts-with(@id,'remove')])[1]").click()

# verify remaining item
items = driver.find_elements("class name", "inventory_item_name")

assert len(items) == 1
print("1 item remaining in cart ✅")





input("please enter to close....")
driver.quit()