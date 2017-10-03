#! python
from PIL import Image
import healpy as hp
from matplotlib.image import pil_to_array
import numpy as np

__author__ = 'Paul Hancock'
__date__ = ''


if __name__ == '__main__':
    grayscale_pil_image = Image.open("shadedrelief.jpg").convert("L")
    image_array = pil_to_array(grayscale_pil_image)
    # reverse the longitude direction so that astro image veiwers plot things the right way around
    image_array = np.fliplr(image_array)
    theta = np.linspace(0, np.pi, num=image_array.shape[0])[:, None]
    phi = np.linspace(-np.pi, np.pi, num=image_array.shape[1])

    nside = 512
    print "Pixel area: %.2f square degrees" % hp.nside2pixarea(nside, degrees=True)

    pix = hp.ang2pix(nside, theta, phi)
    healpix_map = np.zeros(hp.nside2npix(nside), dtype=np.double)
    healpix_map[pix] = image_array

    hp.write_map('earth.fits', healpix_map, coord='C')
