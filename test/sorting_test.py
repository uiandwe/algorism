__author__ = 's0400615'

import pytest
xfail = pytest.mark.xfail

import sorting.sorting


def test_bubble():
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
    s = sorting.sorting()
    print(s.bubble(temp_list))
