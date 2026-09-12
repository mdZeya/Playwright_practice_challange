import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Dashboard import DashboardPage
from Utils.json_reader import read_json




@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def credentials():
    return read_json("PythonPlaywright/data/testdata.json")

@pytest.fixture
def dashboard(page):
    return DashboardPage(page)