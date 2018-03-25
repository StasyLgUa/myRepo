


def test_positive_login(app):
    assert app.login_page.is_this_page()
    app.login_page.username_field.clear()
    app.login_page.username_field.send_keys("admin")

    app.login_page.password_field.clear()
    app.login_page.password_field.send_keys("secret")

    app.login_page.submit_button.click()

    assert app.internal_page.is_this_page()
    #assert "admin" in app.loged_user.text

