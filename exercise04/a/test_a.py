import gcpextract

def test_get_pool(mocker):
    mocker.patch("gcpextract.connect_with_connector", return_value="pool")
    result = gcpextract.connect_with_connector()

    # Assertions to check if the returned data is as expected
    assert result == "pool"
    assert type(result) is str

def test_call_db(mocker):
    mocker.patch("gcpextract.call_db", return_value="w/e")
    result = gcpextract.call_db()

    # Assertions to check if the returned data is as expected
    assert result == "w/e"
    assert type(result) is str