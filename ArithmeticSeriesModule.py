"""
This module contains a function from the set of natural numbers 
to the cartesian product of natural numbers with self.
This function, 'quadratic_series', is bijective.

Too contains the inverse function 'quadratic_series_inv'.
This function, 'quadratic_series_inv', is bijective.

To proof that both functions are inverses of each other,
the module includes the two compositions of the anterior functions.


A naive view of the function:
    
    SetN is the set of natural numbers included 0.
    
    SetN x SetN is the set of 2-tuples of natural numbers.
    
    Quadratic_series is a bijective function.
    
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
of a given group number:
     min_index_from_group(group: int) -> int
     max_index_from_group(group: int) -> int
Their formulas are:
     min_index_from_group(group) = (group * (group + 1)) // 2
     max_index_from_group(group) = (group * (group + 3)) // 2
Then, with the anterior formulas and the index of the series,
we determine the tuple corresponding to the index:
"""


from numpy import longdouble as ldbl
from numpy import ceil
from numpy import floor
from numpy import round
from numpy import sqrt


def min_index_from_group(group: int) -> int:
    """
    Return the minimum index of the group.
    The formula that relations the group
    with the index is:
    group * (group + 3) >= 2 * index >= group * (group + 1).

    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

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
    group * (group + 3) >= 2 * index >= group * (group + 1).

    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

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


def max_group_from_index(index: int) -> int:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    :param index:
    :type index: Natural number: int.
        An index for the series belongs to SetN.
    :return: Natural number.
        The maximum possible group for a given index.
    :rtype: A positive integer or zero: int.
    """
    result: int = int(ceil(ldbl(sqrt(ldbl(8 * index + 9)) - 3) / ldbl(2)))
    return result


def min_group_from_index(index: int) -> int:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    :param index:
    :type index: Natural number: int.
        An index for the series belongs to SetN.
    :return: Natural number.
        The minimum possible group for a given index.
    :rtype: A positive integer or zero: int.
    """
    result: int = int(floor(ldbl(-1 + sqrt(ldbl(1 + 8 * index))) / ldbl(2)))
    return result


def group_from_index(index: int) -> int:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    :param index:
    :type index: Natural number: int.
        An index for the series belongs to SetN.
    :return: Natural number.
        The unique possible group for a given index.
        Returned as an arithmetic mean of the maximum group
        and the minimum group from a given index.
    :rtype: A positive integer or zero: int.
    """
    return int(
        round((min_group_from_index(index) + max_group_from_index(index)) / ldbl(2))
    )


def index_in_group_interval(index: int, group: int) -> bool:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    :param index: Index from SetN.
                Position in the series.
    :type index: Natural number: int.
    :param group: Ordinal accompaniment of the tuple images for successive indexes in the series.
    :type group: Natural number: int.
    :return: True if the index belongs to the group interval, False otherwise.
    :rtype: Boolean.
    """
    return min_index_from_group(group) <= index <= max_index_from_group(group)


def quadratic_series(index: int) -> tuple[int, int]:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    Quadratic bijection function from SetN to SetN x SetN.
    This function establishes the equal cardinal between the two sets.

    :param index: Index from SetN.
                Position in the quadratic series.
    :type index: Natural number: int.
    :return: The corresponding tuple for the natural number index.
    :rtype: Tuple[Natural number, Natural number]: tuple[int, int].
    """
    group: int = int(group_from_index(index))
    pr1st: int = index - min_index_from_group(group)
    pr2nd: int = group - pr1st
    return pr1st, pr2nd


def quadratic_series_inv(pr1st: int, pr2nd: int) -> int:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    Quadratic root bijection function from SetN x SetN to SetN.
    This function is the inverse of the quadratic_series function,
    and it establishes the equal cardinal between the two sets.

    :param pr1st: First component of the 2-tuple from SetN x SetN.
    :type pr1st: Natural number: int.
    :param pr2nd: Second component of the 2-tuple from SetN x SetN.
    :type pr2nd: Natural number: int.
    :return: The corresponding index for the SetN.
    :rtype: Natural number: int.
    """
    group: int = pr1st + pr2nd
    index: int = pr1st + min_index_from_group(group)
    return index


def identity_in_SetN(index: int) -> int:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    Identity bijection function from SetN to SetN, with intermediate SetN x SetN set.
    Quadratic_series o Quadratic_series_inv == Identity: SetN -> SetN x SetN -> SetN.

    :param index: Element from SetN.
    :type index: Natural number: int.
    :return: Element from SetN.
    :rtype: Natural number: int.
    """
    image_of_index: tuple[int, int] = quadratic_series(index)
    return quadratic_series_inv(image_of_index[0], image_of_index[1])


def identity_in_SetN_x_SetN(pr1st: int, pr2nd) -> tuple[int, int]:
    """
    SetN is a name for the set of natural numbers, including the zero number.
    SetN x SetN is the set of 2-tuples of natural numbers.

    Identity bijection function from SetN x SetN to SetN x SetN, with intermediate SetN set.
    Quadratic_series_inv 'o' Quadratic_series == Identity: SetN x SetN -> SetN -> SetN x SetN.

    :param pr1st: First component of an element from SetN x SetN.
    :type pr1st: Natural number: int.
    :param pr2nd: Second component of an element from SetN x SetN.
    :type pr2nd: Natural number: int.
    :return: Tuple element from SetN x SetN.
    :rtype: Tuple[Natural number, Natural number]: tuple[int, int].
    """
    index_image_of_tuple: int = quadratic_series_inv(pr1st, pr2nd)
    return quadratic_series(index_image_of_tuple)


if __name__ == "__main__":
    pass
