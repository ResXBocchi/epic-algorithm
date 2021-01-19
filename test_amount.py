import pytest


def get_max_apples(A, K, L):

    if K > 0 or L > 0:   # if for preventing error when the values of K and L are both 0

        a_index = [n for n in range(len(A))]  # indexes of A list
        k_values = [A[n:n+K] for n in range(len(A)+1-K)]  # list of the fractions of A that K potentially will harvest
        k_values_index = [a_index[n:n+K] for n in range(len(A)+1-K)]  # indexes of K values
        l_values = [A[n:n+L] for n in range(len(A)+1-L)]  # list of the fractions of A that L potentially will harvest
        l_values_index = [a_index[n:n+L] for n in range(len(A)+1-L)]  # indexes of L values

        biggest_amount = 0 # biggest number of apples that can be harvested with given parameters
        index_list = [] # list containing the information about what trees combined gives the best harvest

        # -- Takes the transformed values and do the calculations -- #
        for n in k_values_index:
            for y in range(len(l_values_index)):
                if not any(item in n for item in l_values_index[y]):
                    if sum(k_values[k_values_index.index(n)])+sum(l_values[y]) > biggest_amount:
                        biggest_amount = sum(k_values[k_values_index.index(n)]) + sum(l_values[y])
                        index_list = [(k_values_index[k_values_index.index(n)], l_values_index[y])]
        # --/ Takes the transformed values and do the calculations -- #

        if biggest_amount > 0:
            k_harvest = index_list[0][0]  # list of the trees actually harvested by K - makes easier
            # to show in the front-end the fraction harvested by K
            l_harvest = index_list[0][1]  # list of the trees actually harvested by L - makes easier
            # to show in the front-end the fraction harvested by L
            return biggest_amount, k_harvest, l_harvest
        else:
            return -1
    else:
        return -1


def test_amount_and_indexes():
    assert get_max_apples([3, 4, 1, 7, 8, 5], 2, 3) == (27, [0, 1], [3, 4, 5])
    assert get_max_apples([3, 4, 2, 1, 2, 3, 4, 5], 3, 4) == (23, [0, 1, 2], [4, 5, 6, 7])
    assert get_max_apples([15, 4, 7, 3, 10, 2, 4, 1], 3, 4) == (45, [0, 1, 2], [3, 4, 5, 6])


def test_insufficient_trees():
    assert get_max_apples([2, 3, 5, 1, 2], 3, 3) == -1


def test_all_trees():
    assert get_max_apples([2, 3, 2, 1, 5], 2, 3) == (13, [0, 1], [2, 3, 4])

# Tests like negative values and not numerical characters are done by the front-end before form submission
