from numpy import longdouble as ldbl
from numpy import ceil
from numpy import floor
from numpy import round
from numpy import sqrt

"""
This module contains a function from the set of natural numbers 
to the cartesian product of natural numbers with self.
The naive function:
    
    SetN is the set of natural numbers included 0.
    
    SetN x SetN is the set of 2-tuples of natural numbers.
    
    quadratic_series is a bijective function.
    
    If group is a natural number defined as the sum of the projections of the resultant tuple:
        group = 1st + 2nd, 
    then group represents a group of tuples as images of consecutive indexes of natural numbers,
    under the function quadratic_series.
     
    quadratic_series: SetN  --> SetN x SetN  # group
                       0    |-> ( 0  ,  0 )  # 0
                       1    |-> ( 0  ,  1 )  # 1
                       2    |-> ( 1  ,  0 )  # 1
                       3    |-> ( 0  ,  2 )  # 2
                       4    |-> ( 1  ,  1 )  # 2
                       5    |-> ( 2  ,  0 )  # 2
                       6    |-> ( 0  ,  3 )  # 3
                       7    |-> ( 1  ,  2 )  # 3
                       8    |-> ( 2  ,  1 )  # 3
                       9    |-> ( 3  ,  0 )  # 3
                     ...    |-> ( ..., ...)  # ...
                   index    |-> (1st , 2nd)  # 1st+2nd
               
This module is used to help to determine a formula for quadratic_series and its 
inverse function quadratic_series_inv.

First, we determine the formula for the minimum (and the maximum) index 
of a given group number.
     min_index_from_group(group: int) -> int
     max_index_from_group(group: int) -> int
Their formulas are:
     min_index_from_group(group) = (group * (group + 1)) // 2
     max_index_from_group(group) = (group * (group + 3)) // 2
"""


def min_index_from_group(group: int) -> int:
    """
    Return the minimum index of the group.
    The formula that relations the group
    with the index is:
    group * (group + 3) >= 2 * index >= group * (group + 1)
    :param group: The group represents the sum of
        the denominator, and the numerator of
        the element, minus one.
    :type group: Integer, int. A number for a group of consecutive images.
    :return: The minimum index of the elements
        in the series that is determined by the
        group.
    :rtype: Integer, int. An index.
    """
    return ((group + 1) * group) // 2


def max_index_from_group(group: int) -> int:
    """
    Return the maximum index of the group.
    The formula that relations the group
    with the index is:
    group * (group + 3) >= 2 * index >= group * (group + 1)
    :param group: The group represents the sum of
        the denominator, and the numerator of
        the element, minus one.
    :type group: Integer, int. A number for a group of consecutive images.
    :return: The maximum index of the elements
        in the series that is determined by the
        group.
    :rtype: Integer, int. An index.
    """
    return (group * (group + 3)) // 2


def max_group_from_index(ind: int) -> int:
    result: int = int(ceil(ldbl(sqrt(ldbl(8 * ind + 9)) - 3) / ldbl(2)))
    return result


def min_group_from_index(index: int) -> int:
    result: int = int(floor(ldbl(-1 + sqrt(ldbl(1 + 8 * index))) / ldbl(2)))
    return result


def group_from_index(index: int) -> int:
    return int(round((min_group_from_index(index) + max_group_from_index(index)) / ldbl(2)))


def index_in_group_interval(index: int, group: int) -> bool:
    return min_index_from_group(group) <= index <= max_index_from_group(group)


def quadratic_series(index: int) -> tuple:
    group: int = int(group_from_index(index))
    pr1st: int = index - min_index_from_group(group)
    pr2nd: int = group - pr1st
    return pr1st, pr2nd


def quadratic_series_inv(pr1st: int, pr2nd: int) -> int:
    group: int = pr1st + pr2nd
    index: int = pr1st + min_index_from_group(group)
    return index


def identity_in_SetN(index: int) -> int:
    image_of_index: tuple[int, int] = quadratic_series(index)
    return quadratic_series_inv(
        image_of_index[0],
        image_of_index[1]
    )


def identity_in_SetN_x_SetN(pr1st: int, pr2nd) -> tuple[int, int]:
    index_image_of_tuple: int = quadratic_series_inv(pr1st, pr2nd)
    return quadratic_series(index_image_of_tuple)


if __name__ == "__main__":
    pass
