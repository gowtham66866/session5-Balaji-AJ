# Session 5

The session 5 is on Functional parameter. We learn about positional argument and default argument. We also lean about *args and **kwargs and keyword argument. 

## time_it function

In the assignment we write a time_it function which take a positional arguments, keywords  arguments, *args and **kwargs as parameters. The  parameter send to time_it function should not be changed we define the below parameters in time_it function

1. positional arguments: fn
2. *args
3. **kwargs
4. keyword arguments: repetition 

The time_it function returns the average run time per call . The call is the number of time the fn passed runs. The call are given by repetition



### print function

The print function takes the *args and prints it as an output. The print function does not change the type of *args argument passed into it. we can define sep or seperation ,Default is ' '. sep is optional and specify how to separate the objects, if there is more than one. end is Optional and Specifies what to print at the end. Default is '\n' (line feed)

### squared_power_list

takes base number and give a list of powers of the base number . Starting from parameter start and ending at parameter end. The default for start is 0 and end is 5. We use the ** unpacking to handle the defaults value send for start and end. The function returns a list. for example, if 2 is the number we are calculating power and returning  [1, 2, 4, 8, 16, 32] .

the calculation is not carried for negative numbers the start cannot be lesser than stop and start and stop cannot be negative numbers.

### polygon_area

The polygon area is given number of side and the length of the side as parameter. This function calculates the area of the polygon . The length and number of side cannot be negative. This polygon supports area calculations of upto a hexagon. 



### temp_converter

Converts the temperature from Celsius to Fahrenheit and vis - a -vis. We pass a base temperature and other parameter defining if the temperature is in Celsius or Fahrenheit and converts to the other. does not take negative number.



### speed_converter

converts a speed given in kilometer per hour to the speed parameters defined by the user. takes  default speed dist and time as argumnets. dist can be km/m/ft/yrd, time can be ms/s/m/hr/day









