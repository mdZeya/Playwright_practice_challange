from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open login page
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    # Verify page title
    expect(page).to_have_title("OrangeHRM")

    # Locate elements
    username = page.get_by_role("textbox", name="Username")
    password = page.get_by_role("textbox", name="Password")
    login_button = page.get_by_role("button", name="Login")

    # Verify elements
    expect(username).to_be_visible()

    expect(username).to_be_editable()

    expect(password).to_be_visible()

    expect(password).to_be_editable()

    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # Perform login
    username.fill("Admin")
    password.fill("admin123")
    login_button.click()

    # Verify successful login
    dashboard = page.get_by_role("heading", name="Dashboard")
    expect(dashboard).to_be_visible()

    print("Login successful!")
    print(page.title())

    browser.close()

