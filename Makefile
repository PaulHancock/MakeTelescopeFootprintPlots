
obs_sites.kml:
	wget  http://www.eso.org/~ndelmott/obs_sites.kml

shadedrelief.jpg:
	wget https://github.com/matplotlib/basemap/raw/master/lib/mpl_toolkits/basemap/data/shadedrelief.jpg


earth.fits: shadedrelief.jpg
	python EarthHPX.py

fits: MLO.fits CTIO.fits MWA.fits SALT.fits

%.fits: telescopes.dat
	grep "^$(firstword $(subst ., ,$@))" telescopes.dat | tr "," ' ' | awk '{print "MIMAS --fitsimage -o "$$1".fits +c "$$2" "$$3" " 90-$$4}' | bash