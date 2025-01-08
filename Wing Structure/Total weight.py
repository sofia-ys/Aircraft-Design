from Ixx import CentroidZcontribution
import numpy as np
import constants as con
from numpy import trapezoid
import math
import scipy as sp
from Ixx import Wingbox_lengths
b = con.b
def area(design_choice, y):
    b = con.b
    d1_root = con.d_1
    d2_root = con.d_2
    d3_root = con.d_3
    d4_root = con.d_4
    b = con.b
    if design_choice == 1:
        span_n1 = con.span_n1_1
        n1 = con.n1_1  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_1
        n2 = con.n2_1  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_1
        t1 = con.t1_1
        span_t2 = con.span_t2_1
        t2 = con.t2_1
        span_As = con.span_As_1
        As = con.As_1  # cross sectional area of a stringer
        q = con.q1
    elif design_choice == 2:
        span_n1 = con.span_n1_2
        n1 = con.n1_2  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_2
        n2 = con.n2_2  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_2
        t1 = con.t1_2
        span_t2 = con.span_t2_2
        t2 = con.t2_2
        span_As = con.span_As_2
        As = con.As_1  # cross sectional area of a stringer
        q = con.q2
    elif design_choice == 3:
        span_n1 = con.span_n1_3
        n1 = con.n1_3  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_3
        n2 = con.n2_3  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_3
        t1 = con.t1_3
        span_t2 = con.span_t2_3
        t2 = con.t2_3
        span_As = con.span_As_3
        As = con.As_3  # cross sectional area of a stringer
        q = con.q3
    else:
        span_n1 = con.span_n1_4
        n1 = con.n1_4  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_4
        n2 = con.n2_4  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_4
        t1 = con.t1_4
        span_t2 = con.span_t2_4
        t2 = con.t2_4
        span_As = con.span_As_4
        As = con.As_4  # cross sectional area of a stringer
        q = con.q4

    n1_inter = sp.interpolate.interp1d(span_n1, n1, kind="previous", fill_value="extrapolate")
    n2_inter = sp.interpolate.interp1d(span_n2, n2, kind="previous", fill_value="extrapolate")
    t1_inter = sp.interpolate.interp1d(span_t1, t1, kind="previous", fill_value="extrapolate")
    t2_inter = sp.interpolate.interp1d(span_t2, t2, kind="previous", fill_value="extrapolate")
    As_inter = sp.interpolate.interp1d(span_As, As, kind="previous", fill_value="extrapolate")

    n1 = n1_inter(y)
    n2 = n2_inter(y)
    t1 = t1_inter(y)
    t2 = t2_inter(y)
    As = As_inter(y)

    d1, d2, d3, d4, = Wingbox_lengths(d1_root, d2_root, d3_root, d4_root, b, y)
    alpha = math.atan((d1 - d3) / d2)

    u = d4 * math.tan(alpha)
    if y > q:
        total_area = ((t1 * d1 + d2 * t2 + t1 * d3) + (d2 * t2 / math.cos(alpha))) + (As * (n1 + n2))

    else:
        total_area = ((t1 * d1 + d2 * t2 + t1 * d3) + (d2 * t2 / math.cos(alpha))) + (As * (n1 + n2)) + (
                        t1 * (d1 - u))

    return total_area


step = 0.01
y_vals = np.arange(0, b / 2 + step, step)


def computearea(y_vals):
    return np.array([area(1, y) for y in y_vals])
def totalvolume(y_vals):
    deriv = computearea(y_vals)
    total = trapezoid(deriv, y_vals)
    return total

totalv = totalvolume(y_vals)

print(totalv)