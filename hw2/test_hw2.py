"""
CMSC 14100
Summer 2023

Test code for Homework #2
"""

import hw2
import os
import sys

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position


MODULE = "hw2"


@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_one_and_multiply",
                                            a, x)
    actual = hw2.add_one_and_multiply(a, x)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, h, expected",
                         [(1, 2, 2.094395),
                          (0, 5, 0.0),
                          (3, 0, 0.0),
                          (2.5, 4, 26.17994),
                          (4, 3, 50.26548),
                          (2, 7, 29.32153)])
def test_volume_of_cone(r, h, expected):
    """
    Do a single test for Exercise 1: volume_of_cone
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "volume_of_cone",
                                            r, h,)
    actual = hw2.volume_of_cone(r, h)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("a, b, n, expected",
                         [(0, 5, 0, True),
                          (10, 2, 5, True),
                          (8, 3, 3, False),
                          (20, 0, 10, False),
                          (15, 5, 3, True),
                          (7, 2, 4, False),
                          (100, 10, 11, False)])
def test_is_a_exactly_b_times_n(a, b, n, expected):
    """
    Do a single test for Exercise 2: is_a_exactly_b_times_n.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE,
                                            "is_a_exactly_b_times_n",
                                            a, b, n)
    actual = hw2.is_a_exactly_b_times_n(a, b, n)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

prices = [(9, 6.58125),
 (99, 72.39375),
 (19.99, 14.61769),
 (29.99, 21.93019),
 (49.99, 36.55519),
 (99.99, 73.11769),
 (199.99, 146.24269),
 (499.99, 365.61769),
 (999.99, 731.24269),
 (1999.99, 1462.49269),
 (4999.99, 3656.24269),
 (9999.99, 7312.49269)]


@pytest.mark.parametrize("display_price, expected", prices)
def test_everything_must_go(display_price, expected):
    """
    Do a single test for Exercise 3: checkout_price
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "checkout_price",
                                            display_price)
    actual = hw2.everything_must_go(display_price)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

##### Bone Density classification test cases #####

dexa_results = \
    [(0.6321400420314608, 0.942, 0.122, -2.5398357210535996, 'osteoporosis'),
     (0.9753488559801369, 0.942, 0.122, 0.2733512785257125, 'normal'),
     (0.851034389425335, 0.942, 0.122, -0.7456197588087287, 'normal'),
     (0.7936072042886599, 0.942, 0.122, -1.2163343910765574, 'osteopenia'),
     (0.7654269183544066, 0.942, 0.122, -1.4473203413573228, 'osteopenia'),
     (0.4874616183341276, 0.942, 0.122, -3.7257244398841998, 'osteoporosis'),
     (0.7126990447645103, 0.942, 0.122, -1.8795160265204072, 'osteopenia'),
     (0.8032695096188813, 0.942, 0.122, -1.1371351670583494, 'osteopenia'),
     (0.8218165795591493, 0.942, 0.122, -0.9851100036135297, 'normal'),
     (0.6057247405489949, 0.942, 0.122, -2.7563545856639755, 'osteoporosis')]


@pytest.mark.parametrize("bmd, mean, sd, t_score, category", dexa_results)
def test_t_score(bmd, mean, sd, t_score, category):
    """
    Do a single test for Exercise 4: t_score
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "t_score", bmd)
    expected = t_score
    actual = hw2.t_score(bmd, mean, sd)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("bmd, mean, sd, t_score, category", dexa_results)
def test_is_normal_bmd(bmd, mean, sd, t_score, category):
    """
    Do a single test for Exercise 5: is_normal_bmd
    """
    expected = category.lower() == "normal"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_normal_bmd", bmd)
    actual = hw2.is_normal_bmd(bmd, mean, sd)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

@pytest.mark.parametrize("bmd, mean, sd, t_score, category", dexa_results)
def test_is_osteopenia(bmd, mean, sd, t_score, category):
    """
    Do a single test for Exercise 6: is_osteopenia
    """
    expected = category.lower() == "osteopenia"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_osteopenia", bmd)
    actual = hw2.is_osteopenia(bmd, mean, sd)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

@pytest.mark.parametrize("bmd, mean, sd, t_score, category", dexa_results)
def test_is_osteoporosis(bmd, mean, sd, t_score, category):
    """
    Do a single test for Exercise 7: is_osteopenia
    """
    expected = category.lower() == "osteoporosis"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_osteoporosis", bmd)
    actual = hw2.is_osteoporosis(bmd, mean, sd)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

bmis = [(104.138, 1.655, 38.0201),
 (97.314, 1.752, 31.70349),
 (78.584, 1.515, 34.23804),
 (124.084, 1.764, 39.87665),
 (86.699, 1.776, 27.48705),
 (78.436, 1.602, 30.56261),
 (126.804, 1.622, 48.19825),
 (123.297, 1.677, 43.8416),
 (59.256, 1.652, 21.71262),
 (120.69, 1.727, 40.46566)]


@pytest.mark.parametrize("weight, height, expected", bmis)
def test_bmi(weight, height, expected):
    """
    Do a single test for Exercise 8: bmi
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "bmi", weight, height)
    actual = hw2.bmi(weight, height)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

hip_replacements = [(0.632, 0.942, 0.122, 101.595, 1.566, False),
 (0.975, 0.942, 0.122, 98.369, 1.731, True),
 (0.851, 0.942, 0.122, 125.836, 1.582, False),
 (0.794, 0.942, 0.122, 82.027, 1.601, True),
 (0.765, 0.942, 0.122, 116.624, 1.555, False),
 (0.487, 0.942, 0.122, 118.755, 1.556, False),
 (0.713, 0.942, 0.122, 105.271, 1.773, True),
 (0.803, 0.942, 0.122, 71.278, 1.508, True),
 (0.822, 0.942, 0.122, 118.78, 1.8, True),
 (0.606, 0.942, 0.122, 106.116, 1.612, False)]


@pytest.mark.parametrize("bmd, mean, sd, weight, height, expected", hip_replacements)
def test_consider_hip_replacement(bmd, mean, sd, weight, height, expected):
    """
    Do a single test for Exercise 10: consider_hip_replacement
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "consider_hip_replacement",
                                            bmd)
    actual = hw2.consider_hip_replacement(bmd, mean, sd, weight, height)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

