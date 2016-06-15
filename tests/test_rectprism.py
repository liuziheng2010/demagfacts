from nose.tools import assert_equal, assert_is_not_none, assert_almost_equal
from demagfacts import rectprism

# table for spheroid
    # table = ((2.0, 0.17356),
    #          (3.0, 0.10871),
    #          (4.0, 0.075407),
    #          (5.0, 0.055821),
    #          (6.0, 0.043230),
    #          (7.0, 0.034609),
    #          (8.0, 0.028421),
    #          (9.0, 0.023816),
    #          (10.0, 0.020286),
    #          (11.0, 0.017515))


def test_cube():
    assert_almost_equal(rectprism.dz(1., 1., 1.), 1.0/3.0)

def test_paper_table():
    table = ((2.0, 0.19832),
             (3.0, 0.14036),
             (4.0, 0.10845),
             (5.0, 0.088316),
             (6.0, 0.074466),
             (7.0, 0.064363),
             (8.0, 0.056670),
             (9.0, 0.050617),
             (10.0, 0.045731),
             (11.0, 0.041705))
    for (p, Dz) in table:
        yield assert_almost_equal, rectprism.dz(1.0, 1.0, p), Dz, 5
