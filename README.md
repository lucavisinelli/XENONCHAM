# XENONCHAM

*Code and results for the production of chameleons in the Sun, as well as the detection rate of chameleons at XENON1T.*

The key parts of the computation are:
* Calculation of the flux of chameleons per unit energy due to Primakoff effect at the tachocline;
* Calculation of the cross section for the absorption of chameleons.
* Monte Carlo analysis

The script for generating plots from the results is in [`code/ChameleonFlux.py`]. The first thing to do is to edit [data_path = "../data/"] so that the directory variables point to the right place.

## MontePython

The [montepython](https://github.com/lucavisinelli/XENONCHAM/tree/main/montepython) folder contains the MontePython likelihood we developed. More details are provided in the [MontePython README](https://github.com/lucavisinelli/XENONCHAM/blob/main/montepython/README.md).

### References

If you use this code, please cite the associated paper:
> S. Vagnozzi, L. Visinelli,  P. Brax, A.-C. Davis, & J. Sakstein (2021), "Direct detection of dark energy: the XENON1T excess and future prospects".

### Authors & Contact

Written and maintained by Luca Visinelli and Sunny Vagnozzi.

This repository contains code which is being actively used for research, so in places it may not be 100% clear. If you have any questions whatsoever, or if the code behaves in an unexpected way, please do not hesitate to contact the authors (luca.visinelli@gmail.com and sunny.vagnozzi@ast.cam.ac.uk).


************************************************************************************************

This research was supported by:

   <a href="https://www.kicc.cam.ac.uk/"><img src="https://pbs.twimg.com/profile_images/1107636993033412608/XfxTseD6.jpg"
height="100px"></a>
   <a href="https://www.cam.ac.uk/"><img src="https://www.hoart.cam.ac.uk/images/university-of-cambridge-logo/image_preview"
height="100px"></a>
   <a href="http://w3.lnf.infn.it/"><img src="https://www.trust-itservices.com/sites/default/files/images/logo/INFN2.png"
height="100px"></a>
