# Tunable-laser
In this project, I need to find the optimal parameters (r, f, p) that provide the maximum intensity for different wavelength in single-mode regime and, finally, smooth tuning. If I can extract these parameters, I will get the tunable laser on a chip with range 50 nm.

Now, I'm going to introduce my code:

## Search of maximum λ (15k spectra)

As for code, i do the  I read the number of files with optical spectrum and find the maximum peak with wavelength in each. Then, I extract the parameters corresponding to the wavelength from the name of the file and build the map. From this map, it's apparent what parameters I need to use during the time interval in order to get the tuning.
