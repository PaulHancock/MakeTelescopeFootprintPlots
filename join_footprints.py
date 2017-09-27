#! python
from __future__ import print_function
from astropy.io import fits
import numpy as np

__author__ = 'Paul Hancock'
__date__ = '26/09/2017'


if __name__ == "__main__":
    files = []
    fovs = []
    elims = []
    with open('telescopes.dat') as f:
        for l in f.readlines():
            if l.startswith('#'):
                continue
            line = l.split('#')[0]  # strip comments
            files.append(line.split(',')[0]+'.fits')
            elims.append(float(line.split(',')[3]))
            fovs.append(float(line.split(',')[4]))


    print(files[0])
    hdu = fits.open(files[0])
    for i in range(1, len(files)):
        print('+'+files[i])
        hdu2 = fits.open(files[i])
        # sky_area = 2*np.pi*(1-np.cos(np.radians(90-elims[i])))
        # view_area = 2*np.pi*(1-np.cos(np.radians(fovs[i])))
        fac = (1-np.cos(np.radians(fovs[i]))) / (1-np.cos(np.radians(90-elims[i])))
        for j, row in enumerate(hdu2[1].data):
            hdu[1].data[j][0] += row[0] * fac
    print('-> sum.fits')
    hdu.writeto('sum.fits', overwrite=True)