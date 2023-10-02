"""
CMSC 14100, Autumn 2023
Homework #2

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

"""

import math


def add_one_and_multiply(a, x):
    """
    Add 1 to a, and multiply by x

    Inputs:
        a [int]: an integer value
        x [int]: another integer value


    Returns [int]: result of adding 1 to a and then multiplying by x.
    """
    ### EXERCISE 1 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression

    return None


def volume_of_cone(r,h):
    """
    compute the volume of a cone, given a radius and height

    Inputs:
        r (float): radius
        h (float): height

    Returns: The volume of a cone
    """
    ### EXERCISE 2 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_a_exactly_b_times_n(a, b, n):
    """
    Check if a is the result of b multiplied by n

    Inputs:
        a (int): a value
        b (int): another value
        n (int): a third value

    Returns: True if a is the result of b multiplied by n, False otherwise
    """

    ### EXERCISE 3 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


##############################
# Constants used in Exercise 4
##############################

DISCOUNT_RATE = 0.35
SALES_TAX_RATE = 0.125


def everything_must_go(display_price):
    """
    Given the display_price of a product, calculate the register
    price after discount and sales tax

    Inputs:
        display_price (float): the value of the item ($)

    Return (float): the face value of the bond
    """
    # Do not remove the three lines with assert. They help verify
    # that gross_value, discount, and tax_rate all have sensible values
    assert display_price > 0

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    ### You may define local variables here for use in
    ### the result expression.
    ### Replace "None" with the appropriate expression(s)
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def t_score(bmd, mean, sd):
    """
    Compute the t-score for a given measurement of bone mass density
    and a reference mean and standard deviation.

    Inputs:
        bmd (float): measured bone mass density
        mean (float): reference mean bone mass density
        sd (float): reference standard deviation of bone mass density

    Returns (float): A T-score, measuring the deviation from the reference
    """

    assert bmd > 0

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression

    tscore = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return tscore


def is_normal_bmd(bmd, mean, sd):
    """
    Does the measured bone mass density fall within the normal range
    for the given reference mean and standard deviation?

    Inputs:
        bmd (float): measured bone mass density
        mean (float): reference mean bone mass density
        sd (float): reference standard deviation of bone mass density

    Returns (boolean): Returns False, if the bone mass density is
      not within normal range True otherwise.
    """

    # Do not remove the following line. This assertion help verify
    # that the bmd is valid
    assert bmd > 0

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_osteopenia(bmd, mean, sd):
    """
    Does the measured bone mass density fall within the osteopenia range
    for the given reference mean and standard deviation?

    Inputs:
        bmd (float): measured bone mass density
        mean (float): reference mean bone mass density
        sd (float): reference standard deviation of bone mass density

    Returns (boolean): Returns True, if the bone mass density
        is within osteopenia range False otherwise.

    """
    # Do not remove the following line. This assertion help verify
    # that the bmd is valid
    assert bmd > 0

    ### EXERCISE 7 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_osteoporosis(bmd, mean, sd):
    """
    Does the measured bone mass density fall within the osteoporosis range
    for the given reference mean and standard deviation?

    Inputs:
        bmd (float): measured bone mass density
        mean (float): reference mean bone mass density
        sd (float): reference standard deviation of bone mass density

    Returns (boolean): Returns True, if the bone mass density
        is within osteoporosis range False otherwise.
    """
    # Do not remove the following line. This assertion help verify
    # that the bmd is valid
    assert bmd > 0

    ### EXERCISE 8 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def bmi(weight, height):
    """
    Compute the body mass index (BMI) for a given weight and height.

    Inputs:
        weight (float): weight in kilograms
        height (float): height in meters

        Returns (float): The BMI for the given weight and height.

    """

    ### EXERCISE 9 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def consider_hip_replacement(bmd, mean, sd, weight, height):
    """
    Provide an initial recommendation for hip replacement surgery based on bone
    desnity and body mass index.

    Inputs:
        bmd (float): measured bone mass density
        mean (float): reference mean bone mass density
        sd (float): reference standard deviation of bone mass density
        weight (float): weight in kilograms
        height (float): height in meters

    Returns (boolean): Returns True, if hip replacement is recommended,
      False otherwise.
    """
    # Do not remove the following line. This assertion help verify
    # that the bmd is valid
    assert bmd > 0

    ### EXERCISE 10 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result
