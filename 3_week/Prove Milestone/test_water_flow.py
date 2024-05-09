#Copyright @Erick Orellana

'''Test file to verify if the functions into Water_Flow runs correctly.
'''

from water_flow import water_column_height, pressure_gain_from_water_height, \
                        pressure_loss_from_pipe, pressure_loss_from_fittings, \
                        reynolds_number, pressure_loss_from_pipe_reduction, \
                        convert_kPa_to_psi
from pytest import approx
import pytest


def test_water_column_height():
    '''Test the water_column_height function by calling it
    and comparing the values it returns to the expected values.
    '''

    assert water_column_height(0.0,0.0) == approx(0.0, abs=0.1)
    assert water_column_height(0.0,10.0) == approx(7.5, abs=0.1)
    assert water_column_height(25.0, 0.0) == approx(25.0, abs=0.1)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.1)


def test_pressure_gain_from_water_height():
    '''Test the pressure_gain_from_water_height function by calling it
    and comparing the values it returns to the expected vaules.
    '''

    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.6280, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe():
    '''Teste the pressure_loss_from_pipe function by calling it
    and comparing the values it returns to the expected values.
    '''

    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)




def test_pressure_loss_from_fittings():
    ''''Test the pressure_loss_from_fittings by calling it and comparing 
    the values it returns to the expected values.
    '''

    assert pressure_loss_from_fittings(0.00,3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65,0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65,2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75,2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75,5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
    ''''Test the reynolds_number function by calling it and comparing 
    the values it returns to the expected values.
    '''

    assert reynolds_number(0.048692,0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692,1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692,1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870,1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870,1.75) == approx(500318, abs=1)


def test_pressure_loss_from_pipe_reduction():
    '''Test the pressure_loss_from_pipe_reduction by calling it and 
    comparing the values it returns to the expected values.
    '''

    assert pressure_loss_from_pipe_reduction(0.28687,0.00,1,0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692) == approx(-184.182, abs=0.001)


def test_convert_kPa_to_psi():
    '''Test the convert_kPa_to_psi function by calling it and
    comparing the values it returns to the expected values.
    '''

    assert convert_kPa_to_psi(158.7) == approx(23.0, abs=0.1)
    assert convert_kPa_to_psi(582.0) == approx(84.4, abs=0.1)
    assert convert_kPa_to_psi(36.2) == approx(5.2, abs=0.1)
    assert convert_kPa_to_psi(584.69) == approx(84.8, abs=0.1)


#Call the main function that is part of pytest so that the
#computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])