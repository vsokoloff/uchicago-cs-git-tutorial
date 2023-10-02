'''
Common helper functions for autograders.
'''

import math
import pytest


def gen_recreate_msg(module, function, *params):
    '''
    Generate a message that can be used to recreate a test in ipython3.

    Parameters
        - module: the name of the module containing the function
        - function: the name of the function
        - params: the parameters passed to the function

    Returns
        - a string containing a message that can be used to recreate the test

    Notes
        This function was selected over the other variants because it uses
        f-strings, which are easier to read and write than the alternatives.
    '''
    params = [str(p) if not isinstance(p, str) else f"'{p}'" for p in params]
    params_str = ", ".join(params)

    recreate_msg = (f"\n\nTo recreate this test in ipython3, run:\n"
                    f"  import {module}\n"
                    f"  {module}.{function}({params_str})\n\n")

    return recreate_msg


def check_not_none(actual, recreate_msg=None):
    '''
    Generate error message if the actual value is None. Return None if no
    problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        This function was selected over the other variants because it has a
        more comprehensive error message.
    '''
    msg = ("\n\nThe function returned None when a value "
           "other than None was expected.\n"
           "Common sources of this problem include:\n"
           "  - forgetting to replace the None placeholder in return statements,\n"
           "  - including a print statement rather than a return statement, and\n"
           "  - forgetting to include a return statement.\n")
    
    if recreate_msg is not None:
        msg += recreate_msg

    if actual is None:
        return msg
    else:
        return None


def check_type(actual, expected, recreate_msg=None):
    '''
    Generate error message if the actual value has the wrong type. Return None
    if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected type of the actual value

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        This function was selected over the other variants because it uses
        f-strings, and requires the fewest parameters.
    '''
    actual_type = type(actual)
    expected_type = type(expected)

    msg = (f"\n\nThe function returned a value of the wrong type.\n"
           f"  Expected return type: {expected_type.__name__}\n"
           f"  Actual return type: {actual_type.__name__}\n")
    
    if recreate_msg is not None:
        msg += recreate_msg

    if actual_type != expected_type:
        return msg
    else:
        return None


def check_number(actual, recreate_msg=None):
    '''
    Generate error message if the actual value is not a number. Return None if
    no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested. there
        is no expected value because we are only checking that the actual value
        is an int or a float.

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        No other variants were present.
    '''
    actual_type = type(actual)

    msg = (f"\n\nThe function returned a value of the wrong type.\n"
           f"  Expected return type: an integer or a float.\n"
           f"  Actual return type: {actual_type.__name__}.\n")
    if recreate_msg is not None:
        msg += recreate_msg

    if actual_type not in [int, float]:
        return msg
    else:
        return None


def check_equals(actual, expected, recreate_msg=None):
    '''
    Generate an error if the actual and expected values are not
    equal. Return None if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected value
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        Minor wording differences among the variants.
    '''
    msg = ("\n\nThe actual and expected values do not match\n"
           f"  Expected: {expected}\n"
           f"  Actual: {actual}\n")

    if recreate_msg is not None:
        msg += recreate_msg

    if actual != expected:
        return msg
    else:
        return None


def check_float_equals(actual, expected, recreate_msg=None):
    '''
    Generate an error if the actual and expected values are not roughly equal.
    Return None if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected value
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        This function was selected over the other variants because it uses
        f-strings.
    '''
    msg = (f"\n\nActual ({actual}) and expected ({expected}) "
           f"values do not match.\n")
    if recreate_msg is not None:
        msg += recreate_msg


    # math.isclose(actual, expected):
    if pytest.approx(expected) == actual:
        return None
    else:
        return msg


def check_expected_none(actual, recreate_msg=None):
    '''
    Generate an error if the actual value is not None. Return None if no
    problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message

    Notes
        No other variants were present.
    '''
    msg = "The function returned a value other than the expected value: None."
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if actual is not None:
        return msg
    else:
        return None


def check_result(actual, expected, recreate_msg=None):
    '''
    Comprehensive check of the actual value returned by a function. Return None
    if no problem is found, otherwise an error message.
    
    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected value
        - recreate_msg: a message that can be used to recreate the test
        
    Returns
        - None if no problem is found, otherwise an error message
        
    Notes
        This function was selected over the other variants because it is more 
        comprehensive.
    '''
    # When we expect a result of None
    if expected is None:
        msg = check_expected_none(actual, recreate_msg)
        if msg is not None:
            return msg

    # Checking that the actual value is not None
    msg = check_not_none(actual, recreate_msg)
    if msg is not None:
        return msg

    # Checking that the actual value is the correct type
    msg = check_type(actual, expected, recreate_msg)
    if msg is not None:
        return msg

    # If we expect a float, check that the actual value is close enough
    if isinstance(expected, float):
        msg = check_float_equals(actual, expected, recreate_msg)
        if msg is not None:
            return msg
    # Otherwise, check that the actual value is equal to the expected value
    else:
        msg = check_equals(actual, expected, recreate_msg)
        if msg is not None:
            return msg
        
    return None


def check_dict_keys(actual, expected, recreate_msg=None):
    '''
    Generate an error if the keys in the actual and expected dictionaries do
    not match. Return None if no problem is found.

    Parameters
        - actual: the actual dictionary returned by the function being tested
        - expected: the expected dictionary

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # generate an error if the keys do not match, None otherwise
    rmsg = ("  A key '{}' appears in the expected result\n"
            "  and is missing from the actual result.\n")
    if recreate_msg is not None:
            rmsg += '\n' + recreate_msg
    for expected_key in expected:
        if expected_key not in actual:
            return rmsg.format(expected_key)
    
    rmsg2 = ("  A key '{}' appears in the actual result\n"
             "  that does not appear in the expected result.\n")
    if recreate_msg is not None:
            rmsg2 += '\n' + recreate_msg
    for actual_key in actual:
        if actual_key not in expected:
            return rmsg2.format(actual_key)

    # no error: the keys match
    return None


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    '''
    Generate an error if a list was modified when modifications are
    disallowed.

    Parameters
        - param_name: the name of the parameter being checked
        - before: the value of the parameter before the function was called
        - after: the value of the parameter after the function was called
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message
    '''
    msg = f'You modified the parameter {param_name}, which is not allowed.\n'
    msg += f'  Value before your code: {before}\n'
    msg += f'  Value after your code:  {after}\n'

    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if before != after:
        return msg
    else:
        return None

        
def check_list_length(actual, expected, recreate_msg, desc=""):
    '''
    Generate an error if the actual list is not the same length as the expected
    list. Return None if no problem is found.

    Parameters
        - actual: the actual list returned by the function being tested
        - expected: the expected list
        - recreate_msg: a message that can be used to recreate the test
        - desc: a description of the list being checked
    '''
    if desc:
        msg = (f"The actual length ({len(actual)}) of the list of {desc} does not "
               f"match the expected length ({len(expected)}) of the list of {desc}")
    else:
        msg = f"The actual length ({len(actual)}) does not match the expected length ({len(expected)}).\n"

    if recreate_msg is not None:
        msg +=  '\n' + recreate_msg

    if len(actual) != len(expected):
        return msg
    else:
        return None


def check_1d_iterable(actual, expected, recreate_msg):
    '''
    This function is used to check tuples and lists. Generates an error if the 
    actual iterable is not the same as the expected. Return None if no problem 
    is found.

    Parameters
        - actual: the actual iterable returned by the function being tested
        - expected: the expected iterable
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Check that the actual value is not None
    msg = check_not_none(actual, recreate_msg)
    if msg is not None:
        return msg

    # Check that the actual value is the correct length
    msg = check_list_length(actual, expected, recreate_msg)
    if msg is not None:
        return msg

    # Check that all the elements are the correct type, and equal to the expected
    for actual_val, expected_val in zip(actual, expected):
        msg = check_type(actual_val, expected_val, recreate_msg)
        if msg is not None:
            return msg

        if isinstance(expected_val, float):
            msg = check_float_equals(actual_val, expected_val, recreate_msg)
        else:
            msg = check_equals(actual_val, expected_val, recreate_msg)

        if msg is not None:
            return msg
        
    return None


def check_2d_iterable(actual, expected, recreate_msg):
    '''
    This function is used to check 2D tuples and lists. Generates an error if
    the actual iterable is not the same as the expected. Return None if no
    problem is found. Return the error message if a problem is found.

    Parameters
        - actual: the actual iterable returned by the function being tested
        - expected: the expected iterable
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Check that the actual value is not None
    msg = check_not_none(actual, recreate_msg)
    if msg is not None:
        return msg
    
    # Check that the actual value is the correct length
    msg = check_list_length(actual, expected, recreate_msg)
    if msg is not None:
        return msg
    
    # Check all the sub-iterables
    for actual_sub, expected_sub in zip(actual, expected):
        msg = check_1d_iterable(actual_sub, expected_sub, recreate_msg)
        if msg is not None:
            return msg
        
    return None


def check_dict_values(expected, actual, recreate_msg=None):
    '''
    Function to check the values in a dictionary. Generates an error if the
    actual dictionary is not the same as the expected. Return None if no
    problem is found.

    First, this function checks the keys in the actual and expected dictionaries
    to make sure they match. Then, it checks the values in the actual and
    expected dictionaries to make sure they match.

    Parameters
        - actual: the actual dictionary returned by the function being tested
        - expected: the expected dictionary
        - recreate_msg: a message that can be used to recreate the test

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Check keys
    msg = check_dict_keys(actual, expected, recreate_msg)
    if msg is not None:
        return msg
    
    # Check values
    for key in expected:
        msg = check_type(actual[key], expected[key], recreate_msg)
        if msg is not None:
            return f'Value error at key "{key}"\n{msg}'

        if isinstance(expected[key], float):
            msg = check_float_equals(actual[key], expected[key], recreate_msg)
        else:
            msg = check_equals(actual[key], expected[key], recreate_msg)

        if msg is not None:
            return f'Value error at key "{key}"\n{msg}'
        
    return None
