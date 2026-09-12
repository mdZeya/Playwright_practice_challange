class LoginPage:

    def __init__(self,page):
        self.page = page

        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.page_title = page.get_by_alt_text("company-branding")
        self.forgot_password_button = page.get_by_text("Forgot your password?")

    def login(self,username,password):
        self.username.fill("Admin")
        self.password.fill("admin123")
        self.login_button.click()

    def forgot_password(self):
        self.forgot_password_button.click()

