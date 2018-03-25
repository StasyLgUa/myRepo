from models.group import Group


def test_create_group(app, login):
    group = Group("new name", "new header", "new footer")
    app.open_group_page()
    app.create_group(group)
    assert "A new group has been entered into the address book." in app.message_group_confirm()
    app.return_to_group_page()

