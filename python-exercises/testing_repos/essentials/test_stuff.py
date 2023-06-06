import stuff
import pytest
from unittest import mock
import requests


@pytest.mark.parametrize('x, y, expected', [(2, 4, 6), (3, 4, 7), (9, 2, 11)])
def test_do_maths(x, y, expected):
    assert stuff.do_maths(x, y) == expected


def test_add_fruit(fruits_test_data):
    salad = stuff.add_fruit('mango', fruits_test_data)
    assert 'mango' in salad


def test_how_many_sweets():
    with pytest.raises(stuff.StuffError, match='We need some people to share sweets with!'):
        stuff.how_many_sweets(['caramel', 'humbug'], [])
    response = stuff.how_many_sweets(['bounty','mars', 'snicker', 'oreo'], ['avni', 'chris'])
    assert response==2

def test_find_cat_by_id(monkeypatch):
    mock_cats = [{'id': 1, 'name': 'Zelda'}, {'id': 2, 'name': 'Tigerlily'}]

    monkeypatch.setattr(stuff, "cats", mock_cats)
    result = stuff.find_cat_by_id(2)
    assert result['name'] == 'Tigerlily'


def test_greeting(capsys):
    stuff.greeting('Aki')
    stdout, stderr = capsys.readouterr()
    assert 'Aki' in stdout
    assert stdout == 'Hello, Aki!\n'


def test_fetch_stuff(capsys):
    og_get = requests.get

    mock_response = mock.Mock()
    mock_response.json.return_value = {
        "email": "test@testing.com", "login": "testing"}

    mock_get = mock.Mock(return_value=mock_response)
    requests.get = mock_get

    stuff.fetch_stuff()
    mock_get.assert_called_with('https://api.github.com/users/getfutureproof')

    out, err = capsys.readouterr()
    assert "test@testing.com" in out

    requests.get = og_get


class TestDoMathsCase:
    def test_do_maths(self):
        assert stuff.do_maths(4, 2) == 6

    def test_do_maths_error(self):
        with pytest.raises(stuff.StuffError, match='We can\'t add 4 and two...'):
            stuff.do_maths(4, "two")

# def sheep_translator(phrase):
#     result = f"M{' m'.join([''.join(['a' for char in word]) for word in phrase.split(' ')])}"
#     return result

# def test_sheep_translator():
#     # Test case 1: Basic phrase
#     phrase = "I love sheep"
#     expected_result = "I mmmm mmmm mmmmm"
#     assert sheep_translator(phrase) == expected_result

#     # Test case 2: Empty phrase
#     phrase = ""
#     expected_result = ""
#     assert sheep_translator(phrase) == expected_result

#     # Test case 3: Phrase with multiple spaces
#     phrase = "Sheep  are   fluffy"
#     expected_result = "S mmmm  aaaa  ffffff"
#     assert sheep_translator(phrase) == expected_result

#     # Test case 4: Phrase with special characters
#     phrase = "Sheep!@# are *&^ fluffy"
#     expected_result = "S mmmm!@# aaaa *&^ ffffff"
#     assert sheep_translator(phrase) == expected_result


def test_sheep_translator():
    response = stuff.sheep_translator("hello")
    assert response == "Maaaaa"


# class StuffError(Exception):
#     pass


# def how_many_sweets(sweets, people):
#     if not people:
#         raise StuffError('We need some people to share sweets with!')
#     return len(sweets) / len(people)


# def test_how_many_sweets():
#     # Test case 1: Equal number of sweets and people
#     sweets = ['chocolate', 'candy', 'gummy bear']
#     people = ['Alice', 'Bob', 'Charlie']
#     assert stuff.how_many_sweets(sweets, people) == 1

    # Test case 2: More sweets than people
    # sweets = ['chocolate', 'candy', 'gummy bear', 'marshmallow']
    # people = ['Alice', 'Bob']
    # assert stuff.how_many_sweets(sweets, people) == 2

#     # Test case 3: More people than sweets
#     sweets = ['chocolate']
#     people = ['Alice', 'Bob', 'Charlie']
#     assert stuff.how_many_sweets(sweets, people) == 0.3333333333333333

#     # Test case 4: No people
#     sweets = ['chocolate', 'candy']
#     people = []
#     try:
#         stuff.how_many_sweets(sweets, people)
#     except StuffError as e:
#         assert str(e) == 'We need some people to share sweets with!'
#     else:
#         pytest.fail('Expected StuffError to be raised')

#     # Test case 5: Empty list of sweets
#     sweets = []
#     people = ['Alice', 'Bob']
#     assert stuff.how_many_sweets(sweets, people) == 0

#     # Test case 6: Empty list of sweets and no people
#     sweets = []
#     people = []
#     try:
#         stuff.how_many_sweets(sweets, people)
#     except StuffError as e:
#         assert str(e) == 'We need some people to share sweets with!'
#     else:
#         pytest.fail('Expected StuffError to be raised')
