# pylint: disable=no-name-in-module
"""
This module performs various arithmetic series operations and evaluations.
"""


from ArithmeticSeriesModule import min_index_from_group as min_index
from ArithmeticSeriesModule import max_index_from_group as max_index
from ArithmeticSeriesModule import group_from_index
from ArithmeticSeriesModule import quadratic_series as N2NxN_index
from ArithmeticSeriesModule import quadratic_series_inv as NxN2N_tuple
from ArithmeticSeriesModule import identity_in_SetN as id_SetN
from ArithmeticSeriesModule import identity_in_SetN_x_SetN as id_SetN_x_SetN

if __name__ == "__main__":
    for group in range(0, 10):
        print(f"group {group} has indexes minimum {min_index(group)}"
              f" and maximum {max_index(group)}")
        for index in range(min_index(group), max_index(group) + 1):
            print(f"index {index} has group "
                  f"{group_from_index(index)}")
    for index in range(0, 55):
        pr1st, pr2nd = N2NxN_index(index)
        print(f"s({index}) = ({pr1st},{pr2nd})")
        print(f"s_inv({pr1st},{pr2nd}) = ({NxN2N_tuple(pr1st,pr2nd)})")

    CORRECT: bool = True
    for index in range(0, 10000):
        CORRECT = CORRECT and (id_SetN(index) == index)
    if CORRECT:
        print("Correct evaluation of the identity in SetN by composition"
              " of functions.")
    else:
        print("Wrong evaluation of the identity in SetN by composition of"
              " functions.")        
    CORRECT = True
    for pr1st in range(0, 1000):
        for pr2nd in range(0, 1000):
            CORRECT = CORRECT and (id_SetN_x_SetN(pr1st, pr2nd) == (pr1st, pr2nd))
    if CORRECT:
        print("Correct evaluation of the identity in SetN x SetN by composition"
              " of functions.")
    else:
        print("Wrong evaluation of the identity in SetN x SetN by composition"
              " of functions.")
    # a : ldbl = 64
    # b : ldbl = 80
    # c : ldbl = 5
    # i : ldbl = (-b+sqrt(b**2-4*a*c))/(2*a)
    # print(f"{a}*i^2+{b}*i+{c}==0 =>  i=={i}")
