<h1 align="center">Tunable-laser</h1>

In this project, I need to find the optimal parameters (r, f, p) that provide the maximum intensity for different wavelength in single-mode regime and, finally, smooth tuning. If I can extract these parameters, I will get the tunable laser on a chip with range 30 nm.

Now, I'm going to introduce my code:

## **Search of maximum λ (15k spectra).py** and **Map r(f, λ).py** at p = 0

1) Reading of each spectrum
2) Filtering (Only one peak must be in the spectrum - single-mode regime) 
  ><p>a) Deletion of spectra with weak-intensity peaks (law SNR)
  ><p>b) Deletion of parasitic signals
  ><p>c) Reading of parameters from each file
  ><p>d) Search maximum λ, intensity and full power of spectra
  ><p>e) Saving in file.txt
3) Studying the dependence between λ and parameters (r, f) according to the file.txt

<h1 align="center"><img src="https://user-images.githubusercontent.com/87599571/179037437-b62af617-8094-4c53-9e15-0406a21f5868.png" width="650" height="400" /></h1>

Actually, this map was created for the parameter p = 0. But, if we change this parameter, then the map will shift relative to the diagonals (because of the long experiment can be shown only for small highlighted fragment):

<h1 align="center"><img src="https://user-images.githubusercontent.com/87599571/179039394-2012c081-b859-488f-9815-7d0b494ac2e2.gif" width="350" height="300" /></h1>

To find the optimal parameters, we have to go through each diagonal of the map. Rather, extract the currents in the middle of the diagonals (**See Search currents.py**). Then, we've chosen the main diagonal (**blue line**) and, furhter, for these parameters **r** and **f**, the parameter **p** was varied.

<h1 align="center"><img src="https://user-images.githubusercontent.com/87599571/179046528-66eeeb20-70df-4080-9df1-d70525688ac1.png" width="650" height="400" /></h1>

## Variation of **p** for the currents of main diagonal **r** and **f**:
To simplify this task, I decided to take **r** = **f** and started to change the phase (See). The result of this experiment can be shown on the **Map r(p,λ)**. This map contains the full data needed to change the wavelength smoothly along one diagonal. To define the currents **p**, **r** = **f**, it was important to analyze each splice for **p** and find the middle of each shelf regarding the wavelength.

<h1 align="center">
  <img src="https://user-images.githubusercontent.com/87599571/179276650-3c0e5cea-bc09-471f-83e6-7de83e8bc9cd.gif" width="450" height="350" />
  <img src="https://user-images.githubusercontent.com/87599571/179276222-4f14d440-6e6b-4db5-9354-fe913440c7e4.png" width="500" height="350" /> 
</h1>

If we use these points from map (**r, f, p**), we will get wavelength tuning:

<h1 align="center"><img src="https://user-images.githubusercontent.com/87599571/179279479-e27d985b-db2b-46fd-9f2a-05e889c6a4f0.png" width="350" height="300" /></h1>
