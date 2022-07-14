<h1 align="center">Tunable-laser</h1>

In this project, I need to find the optimal parameters (r, f, p) that provide the maximum intensity for different wavelength in single-mode regime and, finally, smooth tuning. If I can extract these parameters, I will get the tunable laser on a chip with range 30 nm.

Now, I'm going to introduce my code:

## Search of maximum λ (15k spectra) and Map r(f, λ) at p = 0

1) Reading of each spectrum
2) Filtering (Only one peak must be in the spectrum - single-mode regime) 
  ><p>a) Deletion of spectra with weak-intensity peaks (law SNR)
  ><p>b) Deletion of parasitic signals
  ><p>c) Reading of parameters from each file
  ><p>d) Search maximum λ, intensity and full power of spectra
  ><p>e) Saving in file.txt
3) Studying the dependence between λ and parameters (r, f) according to the file.txt

<h1 align="center"><img src="https://user-images.githubusercontent.com/87599571/179037437-b62af617-8094-4c53-9e15-0406a21f5868.png" width="650" height="400" /></h1>

Actually, this map was created for the parameter p = 0. But, if we change this parameter, then the map will shift relative to the diagonals (because of the long experiment it can be shown only for small highlighted fragment):

[Fragment of map](https://user-images.githubusercontent.com/87599571/179039394-2012c081-b859-488f-9815-7d0b494ac2e2.gif)

