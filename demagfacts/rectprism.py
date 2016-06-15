from math import pi, e, log, atan, sqrt
from .helpers import u0


def dz(a, b, c):
    """Compute Dz of a rectangular prism.

    Origin lies at the center of the prism. The prism therefore takes up
    the region (in cartesian coords) -a<x<a, -b<y<b, -c<z<c. Permute
    the coordinates to get the other factors (Dx, Dy).
    """

    return (1/pi) * (_A(a, b, c) +
                     _A(b, a, c) +
                     _B(a, b, c) +
                     _B(b, a, c) +
                     _B(-b, c, a) +
                     _B(-a, c, b) +
                     _C(a, b, c) +
                     _D(a, b, c) +
                     _E(a, b, c) +
                     _F(a, b, c) +
                     _G(a, b, c))


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


def _R(a, b, c):
    return sqrt(a**2 + b**2 + c**2)


def _A(a, b, c):
    r = _R(a, b, c)
    return (b**2 - c**2)/(2*b*c) * log((r-a)/(r+a))


def _B(a, b, c):
    rc = sqrt(a**2 + b**2)
    return (b/(2*c)) * log((rc+a)/(rc-a))


def _C(a, b, c):
    r = _R(a, b, c)
    return 2 * atan(a*b/(c*r))


def _D(a, b, c):
    return (a**3 + b**3 - 2*c**3) / (3*a*b*c)


def _E(a, b, c):
    return _R(a, b, c) * (a**2 + b**2 - 2*c**2) / (3*a*b*c)


def _F(a, b, c):
    return c/(a*b) * (sqrt(a**2 + c**2) + sqrt(b**2 + c**2))


def _G(a, b, c):
    num = (a**2 + b**2)**1.5 + (a**2 + c**2)**1.5 + (b**2 + c**2)**1.5
    return -num / (3*a*b*c)
