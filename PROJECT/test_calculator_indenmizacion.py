#Copyright Erick Orellana BYU - Idaho Student ONLINE CSE 111

import pytest
from Calculator_Indenmizacion import daysbetween, compensation_salary, show_message, days_to_vacations
from pytest import approx
from datetime import date

#Variables 



def test_daysbetween():
    '''Verify that the daysbetween function works correctly
    Parameters: none
    Returns: nothing
    '''

    #Call the daysbetween fucntion and store the returned
    assert daysbetween("2021-12-13", "2024-02-16") == abs(795)
    assert daysbetween("2021-01-01", "2025-01-01") == abs(1461)
    assert daysbetween("1980-05-05", "2045-05-05") == abs(23741)
    assert daysbetween("2000-01-01", "2024-08-01") == abs(8979)
    assert daysbetween('2004-05-09', '2014-05-09')  == abs(3652)
    

def test_compensation_salary():
    '''Verify that the compensation_salary function works correctly
    Parametes: none
    Returns: nothing
    '''
    #A list with many salaries and days
    # salaries = [4000, 3000, 2000, 1000]
    # days = [795, 1461, 23741, 3652]
    # results = [10164.38, 14009.59, 151768.95, 11673.06]

    assert compensation_salary(795, 4000) == approx(10164.38, abs=0.01)
    assert compensation_salary(1461, 3000) == approx(14009.59, abs=0.01)
    assert compensation_salary(23741, 2000) == approx(151768.95, abs=0.01)
    assert compensation_salary(3652, 1000) == approx(11673.06, abs=0.01)


def test_days_to_vacations():
    '''Verify that the days_to_vacations function workds correctly
    Parameters: none
    Retursn: none
    '''

    YEAR = date.today().year

    date1 = date(YEAR, 2, 19)
    date2 = date(YEAR, 3, 25)
    date3 = date(YEAR, 5, 5)

    assert days_to_vacations(str(date1)) == approx(50)
    assert days_to_vacations(str(date2)) == approx(85)
    assert days_to_vacations(str(date3)) == approx(126)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])