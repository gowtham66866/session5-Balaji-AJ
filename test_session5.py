import pytest
import random
import string
import session5
import os
import inspect
import re
import math
from decimal import Decimal

README_CONTENT_CHECK_FOR = ['time_it','print','squared_power_list','polygon_area','temp_converter','speed_converter']


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

    
def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_intentation():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(session5)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert re.search(
            '[a-zA-Z#@""]', space
        ), "Your code intentation does not follow PEP8 guidelines"
        assert (
            len(re.sub(r"[a-zA-Z#@\n\"\"]", "", space)) % 4 == 0
        ), "Your code intentation does not follow PEP8 guidelines"
 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_zero_speed_converter():
    avg1 , ret = session5.time_it("speed_converter", 0, dist='km', time='min',repetitons=100)
    assert ret == 0.0, "speed_converter not implemented properly"

def test_negative_speed_converter():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("speed_converter", -100, dist='km', time='min',repetitons=100)

def test_negative_polygon_area():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("polygon_area", -15, sides = 3, repetitons=100)

def test_negative_polygon_area():
    avg1 , ret = session5.time_it("polygon_area", 0, sides = 3, repetitons=100)
    assert ret == float(0), "polygon_area not implemented properly"

def test_zero_temp_converter():
    avg1 , ret = session5.time_it("temp_converter", 0, temp_given_in = 'f', repetitons=100) 
    assert ret == -18, "temp_converter not implemented properly"

def test_negative_squared_power_list():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("squared_power_list", -2, start=0, end=5, repetitons=5) 

def test_negative_start_squared_power_list():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("squared_power_list", 2, start=-2, end=5, repetitons=5)

def test_negative_end_squared_power_list():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("squared_power_list", 2, start=2, end= -5, repetitons=5)

def test_start_gt_end_squared_power_list():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("squared_power_list", 2, start=5, end= 2, repetitons=5)


def test_squared_negative_repetition():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("squared_power_list", 2, start=5, end= 2, repetitons= -5)

def test_temp_converter_negative_repetition():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("temp_converter", 0, temp_given_in = 'f', repetitons= -100) 


def test_polygon_area_negative_repetition():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("polygon_area", -15, sides = 3, repetitons= -100)

def test_negative_speed_converter():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("speed_converter", 100, dist='km', time='min',repetitons= -100)

def test_temp_converter():
    avg1 , ret = session5.time_it("temp_converter", 98.4 , temp_given_in = 'f', repetitons=100) 
    assert int(ret) == 37, "temp_converter not implemented properly"

def test_speed_converter():
    avg1 , ret = session5.time_it("speed_converter", 100, dist='km', time='min',repetitons=100)
    assert round(ret,2) == 1.67, "speed_converter not implemented properly"

def test_squared_power_not_list():
    avg1,ret = session5.time_it("squared_power_list", 2, start=0, end=5, repetitons=5)
    assert type(ret) == list , "test_squared_power_not_list not passed"

def test_print():
    avg1,ret = session5.time_it("print", 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
    assert ret == "GitPit" , "test_print not passed"

def test_polygon_side_negative():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("polygon_area", 15, sides = -3, repetitons= 100)

def test_temp_converter_other_negative():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("temp_converter", 0, temp_given_in = 'a', repetitons= -100)

def test_incorrect_function_name():
    with pytest.raises(ValueError) as e_info:
        avg1,ret = session5.time_it("temp_converter1", 0, temp_given_in = 'a', repetitons= -100)
        
def test_incorrect_timeit_function_name():
    lines = inspect.getsource(session5.time_it)
    assert lines.find('def time_it(fn, *args, repetitons= 1, **kwargs):') == 0


    

    








