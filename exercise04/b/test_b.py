import firestorewriter

def test_get_pool():

    result = firestorewriter.csv_to_dic("b/location.csv")

    # Assertions to check if the returned data is as expected
    assert result[0] == {'number': '43', 'country': 'Paraguay', 'state': 'Iowa', ' number2': '95957'}
    assert result[-1] == {'number': '18907', 'country': 'Faroe Islands', 'state': 'South Carolina', ' number2': '49187'}