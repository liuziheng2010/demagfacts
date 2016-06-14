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
    -g --geometry=GEOMETRY      'rectprism' is the only supported geometry for
                                now.
"""
from docopt import docopt
import demagfacts as dmf

def cli():
    args = docopt(__doc__)
    a, b, c = (float(args[x]) for x in ('A', 'B', 'C'))

    if args['--geometry'] in (None, 'rectprism'):
        return dmf.rect_prism(a, b, c)
