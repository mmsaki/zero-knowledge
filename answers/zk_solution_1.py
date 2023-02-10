# Zero Knowledge Bootcam
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt


def question_one():
    """
    1. Working with the following set of integers s = {0,1,2,3,4,5,6}
    What is
    a) 4 + 4
    b) 3 x 5
    c) what is the inverse of 3?
    """
    # opereations are caried out by modulo 7
    s = {0, 1, 2, 3, 4, 5, 6}
    p = 7

    a = (4+4) % p
    b = (3*5) % p
    c = pow(3, -1, p) # pyhton internal inverse modular function pow()

    # For c we can use Fermat's little theorem where a^-1 = a^(p-2) mod p
    c = (3**(p-2))%p 

    print(f"Question 1: a={a} b={b} c={c}")


def question_two():
    """
    2. For S = {0,1,2,3,4,5,6}
    Can we consider 'S' and the operation '+' to be a group?
    """
    notes = """
    Simply put a group is a set of elements set(a, b, c, ...) plus a binary operation
    To be concidered a group the combination needs to have the following Properties:
    1. Closure:
      For all a,b in set S, the result of a + b is also in S
    2. Associativity:
      For all a,b and c in set S, (a+b)+c = a+(b+c)
    3. Identity element
      There exists an element e in set S such that, every element a in set S, the equation e + a = a + e = a holds.
      Such an element is unique and thus on speaks of the identity element.
    4. Inverse element
      For each a in set S, there exists an element b in set S, commonly denoted -a (if operations is +) or a**-1 if operator is *, such that a + b = b + a = e, where e is the identity element. 
    """

def questions_three():
    """
    What is -13 mod 5?
    """
    res = -13 % 5
    print(f"Question 3: {res}")


def question_four():
    """
    Polynomials
    For the polynomials x**3 - x**2 + 4x - 12
    Find a the positive root?
    what is the degree of this polymial?
    """
    # def f(x): return x**2 - x + 4
    # res = fsolve(f,2)

    # print(f"Question 4: {res}")


def main():
    question_one()
    question_two()
    questions_three()
    question_four()


main()
