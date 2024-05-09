from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

names = ['Erick', 'Eduardo', 'Jeimy']
family_names = ['Orellana', 'Umana', 'Alvarado']

#Testing of the test 
def test_make_full_name():
    """Test the test_make_full_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert make_full_name('Erick', 'Orellana') == 'Orellana; Erick'
    assert make_full_name('Eduardo', 'Umana') == 'Umana; Eduardo'
    assert make_full_name('Jeimy', 'Alvarado') == 'Alvarado; Jeimy'

def test_extract_family_name():
    """Test the extract_family_name function by
    calling it and comparint the values it returns to the expected values.
    """
    
    assert extract_family_name('Orellana; Erick') == 'Orellana'
    assert extract_family_name('Umana; Erick') == 'Umana'
    assert extract_family_name('Alvarado; Jeimy') == 'Alvarado'

def test_extract_given_name():
    """Test the extract_given_name function by calling it and compariting the values it returns to the expected values.
    """
    assert extract_given_name('Orellana; Erick') == 'Erick'
    assert extract_given_name('Alvarado; Jeimy') == 'Jeimy'
    assert extract_given_name('Umana; Eduardo') == 'Eduardo'
# Call the function is part of pytest so that the
# computures will execute the test functions in this file.
    
pytest.main(["-v", "--tb=line", "-rN", __file__])