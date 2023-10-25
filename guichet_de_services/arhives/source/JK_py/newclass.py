# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:46:59 2020

@author: jk
"""

class NewClass:
       """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """

  def __init__(self, x, y):

    self.x = x

    self.y = y

Ob1 = NewClass("momo", "bobo")

print(Ob1.x)

print(Ob1.y)