#! python
from __future__ import print_function
from astropy.io import fits

__author__ = 'Paul Hancock'
__date__ = '26/09/2017'


if __name__ == "__main__":
    files = []
    with open('telescopes.dat') as f:
        for l in f.readlines():
            if l.startswith('#'):
                continue
            files.append(l.split()[0][:-1]+'.fits')  # telescope name is first col, and has a trailing ','
    print(files[0])
    hdu = fits.open(files[0])
    for f in files[1:]:
        print('+'+f)
        hdu2 = fits.open(f)
        for i, row in enumerate(hdu2[1].data):
            hdu[1].data[i][0] += row[0]
    print('-> sum.fits')
    hdu.writeto('sum.fits', overwrite=True)