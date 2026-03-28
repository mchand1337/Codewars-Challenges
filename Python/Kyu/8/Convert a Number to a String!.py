def number_to_string(num):
    """
    We need a function that can transform a number (integer) into a string.

    What ways of achieving this do you know?
    Examples (input --> output):

    123  --> "123"
    999  --> "999"
    -100 --> "-100"

    """

    return str(num)


print(type(number_to_string(67)))
print(number_to_string(67)) # ans '67'

print(type(number_to_string(79585)))
print(number_to_string(79585)) # ans '79585'

print(type(number_to_string(-79585)))
print(number_to_string(-79585)) # ans '-79585'

print(type(number_to_string(1+2)))
print(number_to_string(1+2)) # ans '3'

print(type(number_to_string(1-2)))
print(number_to_string(1-2)) # ans '-1'

print(type(number_to_string(0)))
print(number_to_string(0)) # ans = '0'