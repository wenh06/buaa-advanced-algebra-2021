"""
"""

from functools import reduce
from typing import Sequence, Union
from numbers import Number

import numpy as np
import sympy as sp


def vandermonde_mat(
    arr: Sequence[Number], latex: bool = False
) -> Union[sp.Matrix, str]:
    """
    computes the Vandermonde matrix defined by the input array,
    i.e. the i-th row is the i-th power of the input array,
    i = 0, 1, ..., n - 1

    Parameters
    ----------
    arr: Sequence[Number],
        the input array that defines the Vandermonde matrix
    latex: bool, default False,
        whether to return the matrix in latex format

    Returns
    -------
    mat: sympy.Matrix or str,
        the Vandermonde matrix

    """
    n = len(arr)
    mat = sp.Matrix(n, n, [item**i for i in range(n) for item in arr])
    if latex:
        return sp.latex(mat)
    return mat


def vandermonde_det(arr: Sequence[Number]) -> Number:
    """
    computes the determinant of a Vandermonde matrix
    defined by the input array,
    i.e. the i-th row is the i-th power of the input array,
    i = 0, 1, ..., n - 1

    Parameters
    ----------
    arr: Sequence[Number],
        the input array that defines the Vandermonde matrix

    Returns
    -------
    Number, the determinant of the Vandermonde matrix

    """
    return reduce(
        lambda a, b: a * b,
        [
            (arr[j] - arr[i])
            for i in range(len(arr) - 1)
            for j in range(i + 1, len(arr))
        ],
    )


def circulant_mat(arr: Sequence[Number], latex: bool = False) -> Union[sp.Matrix, str]:
    """
    computes the circulant matrix defined by the input array,
    i.e. the i-th row is the input array shifted by i positions to the left

    Parameters
    ----------
    arr: Sequence[Number],
        the input array that defines the circulant matrix
    latex: bool, default False,
        whether to return the matrix in latex format

    Returns
    -------
    mat: sympy.Matrix,
        the circulant matrix

    """
    n = len(arr)
    mat = np.vstack([np.concatenate((arr[i:], arr[:i])) for i in range(n)])
    mat = sp.Matrix(mat)
    if latex:
        return sp.latex(mat)
    return mat


def circulant_det(arr: Sequence[Number]) -> Number:
    """
    computes the determinant of a circulant matrix
    defined by the input array,
    i.e. the i-th row is the input array shifted by i positions to the left

    Parameters
    ----------
    arr: Sequence[Number],
        the input array that defines the circulant matrix

    Returns
    -------
    Number, the determinant of the circulant matrix

    """
    # n = len(arr)
    # u = sp.exp(2 * sp.pi * complex(0, 1) / n)
    # sp_arr = sp.Matrix(n, 1, arr)
    # mat = sp.Matrix(n, n, [pow(pow(u, i), j) for i in range(n) for j in range(n)])
    # return reduce(lambda a, b: a * b, mat @ sp_arr)
    return circulant_mat(arr, latex=False).det()


def LagrangePolynomial(
    xs: np.ndarray, ys: np.ndarray, to_poly: bool = True
) -> Union[sp.Poly, sp.Add]:
    """
    computes the Lagrange polynomial of the given points

    Parameters
    ----------
    xs, ys: np.ndarray,
        the points
    to_poly: bool, default True,
        whether to convert the result to sympy.Poly

    Returns
    -------
    poly: sympy.Poly or sympy.Add,
        the Lagrange polynomial of the given points

    """
    X = sp.symbols("x")
    assert len(xs) == len(ys), "The length of `xs` and `ys` must be equal"
    poly = 0
    for k in range(len(xs)):
        t = 1
        for j in range(len(xs)):
            if j != k:
                t = t * ((X - xs[j]) / (xs[k] - xs[j]))
        poly += t * ys[k]
    poly = sp.simplify(poly)
    if to_poly:
        poly = sp.Poly(poly, X)
    return poly


def polyn_discriminant(
    f: Union[sp.Add, sp.Poly], x: sp.Symbol
) -> Union[sp.Add, sp.Number]:
    """
    computes the discriminant of a univariate polynomial

    Parameters
    ----------
    f: sympy.Add or sympy.Poly,
        the univariate polynomial
    x: sympy.Symbol,
        the variable

    Returns
    -------
    pol_det: sympy.Add or sympy.Number,
        the discriminant of the input univariate polynomial `f`

    """
    f = sp.Poly(f, x)
    f_prime = sp.diff(f, x)
    leading_coeff = f.coeffs()[0]
    n = f.degree()
    pol_det = sp.resultant(f, f_prime, x) * (-1) ** (n * (n - 1) // 2) / leading_coeff
    pol_det = sp.simplify(pol_det)
    return pol_det


def sylvester_mat(
    f: Union[sp.Add, sp.Poly],
    g: Union[sp.Add, sp.Poly],
    x: sp.Symbol,
) -> sp.Matrix:
    """
    computes the Sylvester matrix of two univariate polynomials

    Parameters
    ----------
    f, g: sympy.Add or sympy.Poly,
        the two univariate polynomials
    x: sympy.Symbol,
        the variable

    Returns
    -------
    mat: sympy.Matrix,
        the Sylvester matrix of `f` and `g`

    """
    f, g = sp.Poly(f, x), sp.Poly(g, x)
    n, m = f.degree(), g.degree()
    f_coeffs = f.all_coeffs()
    g_coeffs = g.all_coeffs()
    mat = sp.zeros(n + m, n + m)
    for idx in range(m):
        mat[idx : idx + n + 1, idx] = f_coeffs
    for idx in range(n):
        mat[idx : idx + m + 1, m + idx] = g_coeffs
    return mat
