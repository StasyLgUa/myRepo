def test_delete_first_group(app, login):
    app.open_group_page()
    app.delete_group(number=0)
    assert "Group has been removed." in app.message_group_confirm()
    app.return_to_group_page()