from ArithmeticSeriesModule import min_index_from_group as min_index
from ArithmeticSeriesModule import max_index_from_group as max_index
from ArithmeticSeriesModule import min_group_from_index as min_group
from ArithmeticSeriesModule import max_group_from_index as max_group
from ArithmeticSeriesModule import group_from_index
from ArithmeticSeriesModule import quadratic_series as N2NxN_index
from ArithmeticSeriesModule import quadratic_series_inv as NxN2N_tuple
from ArithmeticSeriesModule import identity_in_SetN as id_SetN
from ArithmeticSeriesModule import identity_in_SetN_x_SetN as id_SetN_x_SetN

from numpy import longdouble as ldbl
from numpy import ceil
from numpy import floor
from numpy import round
from numpy import sqrt

if __name__ == "__main__":
    for group in range(0, 10):
        print(
            f"group {group} has indexes minimum {min_index(group)} and maximum {max_index(group)}"
        )
        for index in range(min_index(group), max_index(group) + 1):
            print(
                f"                                     index {index} has group {group_from_index(index)}"
            )
    for index in range(0, 55):
        pr1st, pr2nd = N2NxN_index(index)
        print(f"s({index}) = ({pr1st},{pr2nd})")
        print(f"s_inv({pr1st},{pr2nd}) = ({NxN2N_tuple(pr1st,pr2nd)})")

    correct: bool = True
    for index in range(0, 10000):
        correct = correct and (id_SetN(index) == index)
    if correct:
        print("Correct evaluation of the identity in SetN by composition of functions.")
    else:
        print("Wrong evaluation of the identity in SetN by composition of functions.")

    correct = True
    for pr1st in range(0, 1000):
        for pr2nd in range(0, 1000):
            correct = correct and (id_SetN_x_SetN(pr1st, pr2nd) == (pr1st, pr2nd))
    if correct:
        print("Correct evaluation of the identity in SetN x SetN by composition of functions.")
    else:
        print("Wrong evaluation of the identity in SetN x SetN by composition of functions.")
    # a : ldbl = 64
    # b : ldbl = 80
    # c : ldbl = 5
    # i : ldbl = (-b+sqrt(b**2-4*a*c))/(2*a)
    # print(f"{a}*i^2+{b}*i+{c}==0 =>  i=={i}")
