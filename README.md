# Tunable-laser
In this project, I need to find the optimal parameters (r, f, p) that provide the maximum intensity for different wavelength in single-mode regime and, finally, smooth tuning. If I can extract these parameters, I will get the tunable laser on a chip with range 50 nm.

Now, I'm going to introduce my code:

## Search of maximum λ (15k spectra)

1) Reading of each spectrum
2) Filtering (Only one peak must be in the spectrum - single-mode regime) 
  ><p>a) Deletion of spectra with weak-intensity peaks (law SNR)
  ><p>b) Deletion of parasitic signals
  ><p>c) Reading of parameters from each file
  ><p>d) Search maximum λ, intensity and full power of spectra
  ><p>e) Saving in file.txt
    
