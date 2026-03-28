def make_readable(seconds):
    """
    
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.

    """

    divide_to_whole = 60
    multiply_to_seconds = 60
    
    second = '00'
    minute = '00'
    hour = '00'
    
    quotient, remainder = divmod(seconds, divide_to_whole)
    
    if quotient <= 59:
        minute = quotient
        second = remainder
    elif quotient >= 60:
        second = remainder
        hour, minute = divmod(quotient, divide_to_whole)
    
    hour = str(hour)
    minute = str(minute)
    second = str(second)
    
    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"

    return f"{hour}:{minute}:{second}"

"""

#############################################  Code block for testing ############################################# 

seconds = 359999
divide_to_whole = 60
multiply_to_seconds = 60

second = '00'
minute = '00'
hour = '00'

quotient, remainder = divmod(seconds , divide_to_whole)

print(quotient)
print(remainder)

if quotient <= 59:
    minute = quotient
    second = remainder
    # print(minute)
    # print(second)
    # print(f"{hour}:{minute}:{second}")
elif quotient >= 60:
    second = remainder
    hour, minute = divmod(quotient, divide_to_whole)
    # print(hour)
    # print(type(hour))
    # print(minute)
    # print(second)
    # print(f"{hour}:{minute}:{second}")


# convert to str

hour = str(hour)
minute = str(minute)
second = str(second)

if len(hour) == 1:
    hour = f"0{hour}"
if len(minute) == 1:
    minute = f"0{minute}"
if len(second) == 1:
    second = f"0{second}"


print(hour)
print(type(hour))
print(minute)
print(second)
print(f"{hour}:{minute}:{second}")

#############################################  Code block for testing ############################################# 

"""