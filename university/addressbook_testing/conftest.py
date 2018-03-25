import pytest
from models.addressbook_app import AddressbookApp


@pytest.fixture(scope="session")
def app():
    app = AddressbookApp()
    yield app
    app.close()


@pytest.fixture()
def login(app):
    app.login("admin", "secret")
    yield
    app.logout()


@pytest.fixture()
def init_group(app, init_login):
    app.open_group_page()
    app.create_group("new name", "new header", "new footer")