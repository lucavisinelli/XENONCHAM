# XENONCHAM

*Code and results for the production of chameleons in the Sun, as well as the detection rate of chameleons at XENON1T.*

The key parts of the computation are:
* Calculation of the flux of chameleons per unit energy due to Primakoff effect at the tachocline;
* Calculation of the cross section for the absorption of chameleons.
* Monte Carlo analysis

The script for generating plots from the results is in [`code/ChameleonFlux.py`]. The first thing to do is to edit [data_path = "../data/"] so that the directory variables point to the right place.

### Citation

Please cite the associated paper:
> S. Vagnozzi, L. Visinelli,  P. Brax, A.-C. Davis, & J. Sakstein (2021), "Direct detection of dark energy: the XENON1T excess and future prospects".

### Authors & Contact

Written and maintained by Luca Visinelli and Sunny Vagnozzi.

This repository contains code which is being actively used for research, so in places it may not be 100% clear. If you have any questions whatsoever, or if the code behaves in an unexpected way, please do not hesitate to contact the authors (luca.visinelli@gmail.com and sunny.vagnozzi@ast.cam.ac.uk).
