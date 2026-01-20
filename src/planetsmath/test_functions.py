# SPDX-FileCopyrightText: 2022 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from .functions import sum_function


def test_sum_function():
    assert sum_function([1, 2, 3, 4, 5]) == 15.0  # testing for changes
    assert sum_function([1, 2.2, 3, 4, 5]) == 15.2
    assert sum_function([-1, 2, 3, 4, 5]) == 13
