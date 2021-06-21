
obs_sites.kml:
	wget  http://www.eso.org/~ndelmott/obs_sites.kml

shadedrelief.jpg:
	wget https://github.com/matplotlib/basemap/raw/master/lib/mpl_toolkits/basemap/data/shadedrelief.jpg


earth.fits: shadedrelief.jpg EarthHPX.py
	python EarthHPX.py

fits: MLO.fits CTIO.fits MWA.fits SALT.fits

AstroSmall.fits: FORCE
	#MIMAS +p 76.671 -66.7033 76.671 14.7033 156.671 14.7033 156.671 -66.7033 -o AstroSmall.mim
	MIMAS +p 272.039701555 -76.7033 155.57684661 23.2967 77.7651533903 23.2967 -38.6977015545 -76.7033 -o AstroSmall.mim
	MIMAS +r AstroSmall.mim --fitsimage -o AstroSmall.fits

%.fits: telescopes.dat
	grep "^$(firstword $(subst ., ,$@))" telescopes.dat | tr "," ' ' | awk '{print "MIMAS --fitsimage -o "$$1".fits +c "360-$$2" "$$3" " 90-$$4}' | bash

FORCE: