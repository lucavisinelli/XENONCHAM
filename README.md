# XENONCHAM

*Code and results for the production of chameleons in the Sun, as well as the detection rate of chameleons at XENON1T.*

The key parts of the computation are:
* Calculation of the flux of chameleons per unit energy due to Primakoff effect at the tachocline
* Calculation of the cross section for the absorption of chameleons.
* Monte Carlo analysis (see the [montepython](https://github.com/lucavisinelli/XENONCHAM/tree/main/montepython) folder)

The script for generating plots from the results is in [`code/ChameleonFlux.py`]. The first thing to do is to edit [data_path = "../data/"] so that the directory variables point to the right place.

## MontePython

The [montepython](https://github.com/lucavisinelli/XENONCHAM/tree/main/montepython) folder contains the MontePython likelihood we developed. More details are provided in the [MontePython README](https://github.com/lucavisinelli/XENONCHAM/blob/main/montepython/README.md).

### References

If you use this code, please cite the associated paper:
> S. Vagnozzi, L. Visinelli,  P. Brax, A.-C. Davis, & J. Sakstein (2021), "Direct detection of dark energy: the XENON1T excess and future prospects".

### Authors & Contact

Written and maintained by Luca Visinelli and Sunny Vagnozzi.

This repository contains code which is being actively used for research, so in places it may not be 100% clear. If you have any questions whatsoever, or if the code behaves in an unexpected way, please do not hesitate to contact the authors at [luca.visinelli@gmail.com](mailto:luca.visinelli@gmail.com) [sunny.vagnozzi@ast.cam.ac.uk](mailto:sunny.vagnozzi@ast.cam.ac.uk) (unless you're a robot, of course).


************************************************************************************************

We acknowledge the support of:

   <a href="https://www.cam.ac.uk/"><img src="https://www.hoart.cam.ac.uk/images/university-of-cambridge-logo/image_preview"
height="120px"></a>
   <a href="https://www.kicc.cam.ac.uk/"><img src="https://pbs.twimg.com/profile_images/1107636993033412608/XfxTseD6.jpg"
height="120px"></a>
   <a href="https://www.ast.cam.ac.uk/"><img src="https://sciencesprings.files.wordpress.com/2020/10/u-cambridge-ioa-logo.png?w=200"
height="120px"></a>
   <a href="https://kavlifoundation.org/"><img src="https://www.aps.org/meetings/march/images/logo-kavli.png"
height="120px"></a>
   <a href="https://www.newtontrust.cam.ac.uk/"><img src="https://www.newtontrust.cam.ac.uk/sites/www.newtontrust.cam.ac.uk/files/styles/leading/public/images/INTmarksmall.png?itok=tNSe1-Sw"
height="120px"></a>
   <a href="http://w3.lnf.infn.it/"><img src="https://www.trust-itservices.com/sites/default/files/images/logo/INFN2.png"
height="120px"></a>
   <a href="https://erc.europa.eu/"><img src="https://erc.europa.eu/sites/default/files/LOGO_ERC.jpg"
height="120px"></a>
   <a href="https://web.infn.it/fellini/"><img src="https://scholarship-positions.com/wp-content/uploads/2018/06/FELLINI-Fellowship.png"
height="120px"></a>
   <a href="https://www.nwo.nl/en"><img src="https://images.squarespace-cdn.com/content/v1/592d67b65016e1bf41b13f96/1496395663632-7ZKH4T7MPTX6EPV1YH92/ke17ZwdGBToddI8pDm48kPALBGyU-J1y7KdYWzUZRhxZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PIsV_1YvFREPWlQ7fWmbarGd3mXHtHh4g9cxHFgfMv3ig/nwo-logo.png?format=500w"
height="120px"></a>
