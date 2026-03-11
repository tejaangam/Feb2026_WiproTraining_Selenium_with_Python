def test_user_creation(user):
    print("[test] running test")

    assert "id" in user
    assert user["name"] == "Test User"
