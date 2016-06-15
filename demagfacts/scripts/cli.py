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
    -s --simple         Don't print out formatted table, just numerical values
    -m=MAGNETIZATION    Sample saturation magnetization in Tesla 
                        u0 x Msat(A/m) = Msat (Tesla)
"""
from docopt import docopt
from demagfacts import rectprism
from tabulate import tabulate

def cli():
    args = docopt(__doc__)
    msat = float(args['-m'])

    # Note: divide by two because formula takes side half-lengths not lengths!
    a, b, c = (float(args[x])/2 for x in ('A', 'B', 'C'))

    permutations = ((a, b, c), (c, a, b), (b, c, a))
    ds = (rectprism.dz(*xs) for xs in permutations)
    if msat:
        es = (rectprism.energy(*xs, msat=msat)/1000.0 for xs in permutations)
    labs = ('dz', 'dy', 'dx')

    if args['--simple']:
        return None
    else:
        table = (row for row in zip(labs, ds, es))
        return tabulate(table, headers=('', 'Dxi', 'E(kJ/m^3'))

        
