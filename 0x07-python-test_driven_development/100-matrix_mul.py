#!/usr/bin/python3
"""
The 'matrix_mul' module
Defines a function trhat multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies m_a by m_b"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for rows in m_a:
        if not isinstance(rows, list):
            raise TypeError('m_a must be a list of lists')
        if len(rows) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for num in rows:
            if not isinstance(num, (int, float)):
                raise TypeError('m_a should contain only integers or floats')

    for rows in m_b:
        if not isinstance(rows, list):
            raise TypeError('m_b must be a list of lists')
        if len(rows) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for num in rows:
            if not isinstance(num , (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_ab = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            res = 0
            for k in range(len(m_b)):
                res += m_a[i][k] * m_b[k][j]
            m_ab[i].append(res)

    return m_ab
