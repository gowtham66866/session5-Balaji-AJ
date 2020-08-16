#!/usr/bin/env python
# coding: utf-8
# In[70]:
from datetime import datetime
from math import tan, pi
import time

def squared_power_list(*args, **kwargs):
    base_number = args[0]
    b = kwargs
    l = {'start':0,'end':5,**b}    
    start_power,end_power = l.values()
    if base_number < 0 or start_power < 0 or end_power < 0 or start_power > end_power:
        raise ValueError ( "This is not a positive number!!" )
    total_value = []
    for i in range(start_power,end_power+1):
        total_value.append(base_number**i)    
    return total_value

def polygon_area(*args, **kwargs):
    side_length =args[0]
    sides = kwargs['sides']
    if side_length < 0 or sides < 0 :
        raise ValueError ( "This is not a positive number!!" )
    polygon_area = sides * (side_length ** 2) / (4 * tan(pi / sides))
    return polygon_area

def speed_converter(*args, **kwargs):
    default_speed = args[0]
    dist_x = kwargs['dist']
    time_x = kwargs['time']

    if default_speed < 0:
        raise ValueError ( "This is not a positive number!!" )

    if dist_x=='km' and time_x == 'ms':
        return default_speed/(60*60*60)
    elif dist_x=='km' and time_x == 'sec':
        return default_speed/(60*60)
    elif dist_x=='km' and time_x == 'min':
        return default_speed/(60)
    elif dist_x=='km' and time_x == 'hr':
        return default_speed
    elif dist_x=='km' and time_x == 'day':
        return default_speed*24

    elif dist_x=='m' and time_x == 'ms':
        return default_speed*0.277778/60
    elif dist_x=='m' and time_x == 'sec':
        return default_speed*0.277778
    elif dist_x=='m' and time_x == 'min':
        return default_speed*0.277778*60
    elif dist_x=='km' and time_x == 'hr':
        return default_speed*0.277778*60*60
    elif dist_x=='m'and time_x == 'day':
        return default_speed*0.277778*60*60*24

    elif dist_x=='ft' and time_x == 'ms':
        return default_speed*0.91134/60
    elif dist_x=='ft' and time_x == 'sec':
        return default_speed*0.91134
    elif dist_x=='ft' and time_x == 'min':
        return default_speed*0.91134*60
    elif dist_x=='ft' and time_x == 'hr':
        return default_speed*0.91134*60*60
    elif dist_x=='ft' and time_x == 'day':
        return default_speed*0.91134*60*60*24

    elif dist_x=='yrd' and time_x == 'ms':
        return default_speed*0.303781/60
    elif dist_x=='yrd' and time_x == 'sec':
        return default_speed*0.303781
    elif dist_x=='yrd' and time_x == 'min':
        return default_speed*0.303781*60
    elif dist_x=='yrd' and time_x == 'hr':
        return default_speed*0.303781*60*60
    elif dist_x=='yrd' and time_x == 'day':
        return default_speed*0.303781*60*60*24

def temp_converter(*args,**kwargs):
    degree = args[0]
    if degree < 0 :
        raise ValueError ( "This is not a positive number!!" )
    i_convention= kwargs['temp_given_in']    
    if i_convention.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit"
    elif i_convention.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        o_convention = "Celsius"
    else:
        quit()
    return result

def time_it(fn, *args, repetitons= 1, **kwargs):
    result=0.0
    if repetitons < 0 :
        raise ValueError ( "Repetitions not a positive number!!" )

    if fn == "print":
        t1 = time.perf_counter()
        for i in range(repetitons):
            print(*args,**kwargs) 
            result='GitPit'
        t2 = time.perf_counter()

    elif fn == "squared_power_list": 
        func = eval(fn)
        t1 = time.perf_counter()
        for i in range(repetitons):            
            result = func(*args,**kwargs)           
        t2 = time.perf_counter()

    elif fn == "polygon_area":
        func = eval(fn)
        t1 = time.perf_counter()
        for i in range(repetitons):
            result = func(*args,**kwargs)
        t2 = time.perf_counter()

    elif fn == "temp_converter":
        func = eval(fn)
        t1 = time.perf_counter()
        for i in range(repetitons):
            result = func(*args,**kwargs)
        t2 = time.perf_counter()

    elif fn ==  "speed_converter":
        func = eval(fn)
        t1 = time.perf_counter()      
        for i in range(repetitons):
            result = func(*args,**kwargs)
        t2 = time.perf_counter()    
    return ((t2-t1)/repetitons,result)