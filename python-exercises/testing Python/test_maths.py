import math
import stuff 

import pytest


def test_sqrt():
    num = 49
    assert math.sqrt(num) == 7
    
def test_square():
    num = 7
    assert 7*7 == 49
    
def test_equality():
    assert 11 == 11
    
def test_is_greater():
    assert 16 > 15
    
@pytest.mark.parametrize('x, y, expected', [(2, 4, 6), (3, 4, 7), (9, 2, 11)])
def test_do_maths(x, y, expected):
    assert stuff.do_maths(x, y) == expected

    
def test_how_many_sweets():
     with pytest.raises(stuff.StuffError, match='We need some people to share sweets with!'):
        stuff.how_many_sweets(['caramel', 'humbug'], [])

def test_cli(capsys):
    stuff.greeting('Avni')
    out, err = capsys.readouterr()
    assert out == 'Hello, Avni!\n'

#MoneyPatch

def test_find_cat_by_id(monkeypatch):
    mock_cats = [{'id': 1, 'name': 'Zelda'}, {'id': 2, 'name': 'Tigerlily'}]

    monkeypatch.setattr(stuff, "cats", mock_cats)
    result = stuff.find_cat_by_id(2)
    assert result['name'] == 'Tigerlily'

# def test_find_cat_by_id(monkeypatch):
#     This line defines a test function named test_find_cat_by_id that takes a monkeypatch argument. This function is likely part of a test suite written using a testing framework like pytest. The monkeypatch argument is used for modifying attributes or behavior during testing.


# mock_cats = [{'id': 1, 'name': 'Zelda'}, {'id': 2, 'name': 'Tigerlily'}]
# This line creates a list called mock_cats that contains two dictionaries. Each dictionary represents a cat and has an 'id' and a 'name' attribute.


# monkeypatch.setattr(stuff, "cats", mock_cats)
# This line uses the monkeypatch object to modify the attribute of an object or module. In this case, it sets the attribute cats of the stuff module to mock_cats. This allows the test to override the original cats data with the mock_cats data for testing purposes.


# result = stuff.find_cat_by_id(2)
# This line calls the find_cat_by_id() function/method from the stuff module, passing 2 as the argument. It is attempting to find a cat with the ID value of 2 using the overridden cats data.


# assert result['name'] == 'Tigerlily'
# This line asserts that the value of the 'name' attribute in the result dictionary (the cat found with ID 2) is equal to 'Tigerlily'. If the assertion fails, it will raise an exception indicating a test failure.
# In summary, this test function is mocking a list of cats, setting it as the cats attribute of the stuff module using monkeypatch, and then calling the find_cat_by_id() function to search for a cat with ID 2. Finally, it asserts that the name of the found cat is 'Tigerlily'.


        
# def test_do_maths():
#     assert stuff.do_maths(4, 2) == 6

# def test_add_fruit():
#     salad = stuff.add_fruit('mango')
#     assert 'mango' in salad

