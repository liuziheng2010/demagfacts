from math import pi, e, log, atan, sqrt, acos, asin
from scipy.special import ellipkinc, ellipeinc
# from .helpers import u0


def D(a, b, c):
    """Compute Dz of a ellipsoid.

    This formula works in general, no assumptions are imposed on the input
    ellipsoid except that  ** a >= b >= c > 0**.

    Args:
        a (float):      x direction semiaxis.
        b (float):      y direction semiaxis
        c (float):      z direction semiaxis
    """

    F = ellipkinc
    E = ellipeinc

    assert a >= b
    assert b >= c
    assert c > 0

    cos_t  = c/a
    assert acos(cos_t) >= 0 
    assert acos(cos_t) <= pi/2
    cos_p = b/a
    assert acos(cos_p) >= 0 
    assert acos(cos_p) <= pi/2
    sin_a = k = ((1 - (b/a)**2) / (1 - (c/a)**2))**0.5
    assert asin(sin_a) >= 0 
    assert asin(sin_a) <= pi/2
    sin_t = (1 - cos_t**2)**0.5
    sin_p = (1 - cos_p**2)**0.5
    cos_a = (1 - sin_a**2)**0.5

    phi = acos(cos_p)
    theta = acos(cos_t)

    _A = cos_p * cos_t / (sin_t**3 * sin_a**2)
    _B = sin_a**2 * sin_t * cos_t / cos_p

    Dx = _A * (F(phi, k) - E(phi, k))
    Dy = _A/cos_a**2 * (E(phi, k) - cos_a**2 * F(phi, k) - _B)
    Dz = _A * (sin_t * cos_p / cos_t - E(phi, k))

    return (Dx, Dy, Dz)
    

def energy(a, b, c, msat):
    """Compute the self energy for a rectangular prism magnetized in the c 
    direction.

    Args:
        a, b, c (float):    Half lengths of the x, y, z edges respectively

        msat (float):       Saturation magnetization of the FM in Tesla. If
                            you have magnetization in A/m just multiply by
                            u0 (magnetic constant).
    """
    return msat**2 / (2*u0) * dz(a, b, c)

res = D(1.2, 1.1, 1.0)
print(res)
print(sum(res))
