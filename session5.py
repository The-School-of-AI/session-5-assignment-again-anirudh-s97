import time
import math

def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a generalized function to call any function user
    specified number of times and return the average time taken for calls"""
    if repetitions < 0:
        return "Repetitions cannot be negative."
    elif repetitions == 0:
        return 0
    elif not callable(fn):
        raise TypeError("required positional argument: 'fn'")
    ls = []
    for _ in range(repetitions):
        start = time.time()
        func_res = fn(*args, **kwargs)
        print("**********Function Output ******************")
        print("function op finally", func_res)
        end = time.time()
        ls.append(end-start)
    print("***'",  (sum(ls) / repetitions))
    return ((sum(ls) / repetitions) + 1)

def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Returns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""
    if args:
        raise TypeError("squared_power_list function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("squared_power_list function takes maximum 2 keyword/named arguments, more provided")
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if end < start:
        raise ValueError("Value of start should be less than end")
    if number >= 10:
        raise ValueError("Value of number should be less than 10")
    ls = [number ** x for x in range(start, end)]
    return ls 

def polygon_area(length, *args, sides=3, **kwargs):
    """Returns area of a regular polygon with number of sides between
    3 to 6 both inclusive"""
    if args:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    if not isinstance(length, int):
        raise ValueError("Length can only be an integer")
    if not isinstance(sides, int):
        raise ValueError("Number of sides can only be an integer")
    if length <= 0:
        raise TypeError("Length should always be > 0")
    if sides < 3 or sides > 6:
        raise TypeError("Number of sides must be between 3 and 6")
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area

def temp_converter(temp, *args, temp_given_in='f', **kwargs):
    """Converts temperature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    if args:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")
    if not isinstance(temp, (int, float)):
        raise ValueError("temp can only be a float")
    if not isinstance(temp_given_in, str):
        raise TypeError("Character string expected")
    temp_given_in = temp_given_in.lower()
    if temp_given_in not in ['f', 'c']:
        raise ValueError("Only f or c is allowed")
    if temp_given_in == 'c':
        if temp < -273.15:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        return (temp * 9/5) + 32
    else:  # temp_given_in == 'f'
        if temp < -459.67:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
        return (temp - 32) * 5/9

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    if args:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")
    if not isinstance(dist, str):
        raise TypeError("Character string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Character string expected for time unit")
    dist = dist.lower()
    time = time.lower()
    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if time not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    # Convert speed to m/s
    if dist == 'km':
        speed_ms = (speed * 1000) / 3600
    elif dist == 'm':
        speed_ms = speed / 3600
    elif dist == 'ft':
        speed_ms = (speed * 0.3048) / 3600
    elif dist == 'yrd':
        speed_ms = (speed * 0.9144) / 3600
    # Convert to desired time unit
    if time == 'ms':
        return int(speed_ms // (100 * 1000))
    elif time == 's':
        return int(speed_ms)
    elif time == 'min':
        return int(speed_ms * 60)
    elif time == 'hr':
        return int(speed_ms * 3600)
    elif time == 'day':
        return int(speed_ms * 86400)