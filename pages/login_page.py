class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element("id", "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("id", "password").send_keys(password)

    def click_login(self):
        self.driver.find_element("id", "login-button").click()
        
    def is_login_successful(self):
        return "inventory" in self.driver.current_url
    
    def is_login_failed(self):
        return "inventory" not in self.driver.current_url