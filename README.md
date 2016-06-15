# Install #
  - Clone to your computer and open the directory.
  - `python3 setup.py install`

# Examples #
  - From the command line run `demagfacts A B C` where the letter arguments
    are the x, y and z dimensions of the object.
  - Add the `-m <magnetization in Tesla>` parameter to also get a list of
    demagnetization energy densities.
  - By default the geometry is assumed to be a rectangular prism. There will
    also be an option for ellipsoids as there is an analytical solution for
    that geometry also.

# Rectangular Prism Geometry #

  - Completes the same calculation as [this javascript calculator.][1]
  - [Originally published by A. Aharoni in JAP][2]



 [1]: http://www.magpar.net/static/magpar/doc/html/demagcalc.html
 [2]: http://scitation.aip.org/content/aip/journal/jap/83/6/10.1063/1.367113

# Ellipsoid Geometry #

  - To be implemented.
