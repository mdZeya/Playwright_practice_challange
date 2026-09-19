import pytest
from playwright.sync_api import expect,Page

@pytest.mark.parametrize(
    "test_data",
    [
        "valid_user",
        "invalid_user1",
        "invalid_user2",
        "invalid_user3",
        "invalid_user4",
        "invalid_user5",
        "invalid_user6"
    ]
)

# @pytest.mark.parametrize("test_data",[
#     {
#   "username" : "Admin",
#   "password" : "admin123",
#     "expected": "success"
#     },
# {
#     "username" : "Admin",
#     "password" : "wrong",
#     "expected" : "fail"
#   },
#  {
#     "username" : "wrong",
#     "password" : "admin123",
#     "expected" : "fail"
#  },
#   {
#     "username" : "",
#     "password" : "",
#     "expected" : "fail"
#   },
#   {
#     "username" : "worng",
#     "password" : "wrong",
#     "expected" : "fail"
#   },
#   {
#     "username" : "Admin",
#     "password" : "",
#     "expected" : "fail"
#   },
#  {
#     "username" : "",
#     "password" : "admin123",
#     "expected" : "fail"
#   }
# ])

def test_valid_login(login_page, credentials, test_data):
    login_page.page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    username = credentials[test_data]["username"]
    password = credentials[test_data]["password"]
    expected = credentials[test_data]["expected"]

    login_page.login(username, password)

    if expected == "success":
        expect(login_page.page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    else:
        expect(login_page.page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

def test_forgot_password(login_page):
    login_page.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.forgot_password()
    expect(login_page.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")

def test_Admin_page(login_page,dashboard):
    login_page.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    dashboard.Admin_click()
    expect(dashboard.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

