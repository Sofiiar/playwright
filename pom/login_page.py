class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, name, password):
        self.page.click("[data-test=\"username\"]")
        self.page.fill("[data-test=\"username\"]", name)
        self.page.click("[data-test=\"password\"]")
        self.page.fill("[data-test=\"password\"]", password)
        self.page.click("[data-test=\"login-button\"]")
