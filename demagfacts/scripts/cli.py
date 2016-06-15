# -*- coding: utf-8 -*-
"""
Computer a demagnetization factor. 

Usage:
    demagfacts.py --help
    demagfacts.py [options] A B C

Arguments:
    A               Length of x side
    B               Length of y side
    C               Length of z side

Options:
    -s --simple         Don't print out formatted table, just numerical values.
                        If -m is passed, the values will be ((dz, Ez), ...) and
                        if -m is not passed the values will be (dz, dy, dx)
    -m=MAGNETIZATION    Sample saturation magnetization in Tesla 
                        u0 x Msat(A/m) = Msat (Tesla)
    -d=COORD            x, y or z to just return Dx, Dy, or Dz. Note, you can
                        also pass this as '-dz' for example to look nice.
"""
from docopt import docopt
from demagfacts import rectprism
from tabulate import tabulate

def cli():
    args = docopt(__doc__)
    try:
        msat = float(args['-m'])
    except TypeError:
        msat = None
    just_d = args['-d']

    # Note: divide by two because formula takes side half-lengths not lengths!
    a, b, c = (float(args[x])/2 for x in ('A', 'B', 'C'))

    permutations = ((a, b, c), (c, a, b), (b, c, a))
    ds = list(rectprism.dz(*xs) for xs in permutations)
    if msat:
        es = (rectprism.energy(*xs, msat=msat)/1000.0 for xs in permutations)
    else:
        es = ['-'] * 3
    labs = ('dz', 'dy', 'dx')

    if just_d:
        case = {'x': 2, 'y': 1, 'z': 0}
        return ds[case[just_d]]
    elif args['--simple']:
        if msat:
            return list(zip(ds, es))
        else:
            return ds
    else:
        table = (row for row in zip(labs, ds, es))
        return tabulate(table, headers=('', 'Dxi', 'E(kJ/m^3)'))

        
