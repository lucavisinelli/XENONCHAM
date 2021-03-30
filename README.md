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

   <a href="http://www.okc.albanova.se/"><img src="http://www.okc.albanova.se/polopoly_fs/1.327382.1491483655!/image/image.jpg_gen/derivatives/logotype_h130/image.jpg"
height="100px"></a>
   <a href="https://www.su.se/"><img src="http://resources.mynewsdesk.com/image/upload/t_open_graph_image/ayjgabd4qxqbpj4pu4nl.jpg"
height="100px"></a>
      <a href="https://www.nordita.org/"><img src="https://yt3.ggpht.com/a-/AJLlDp3bQ-UG2qVRBjqfsEbsUaDs_fd8yBPkMnPCXg=s900-mo-c-c0xffffffff-rj-k-no"
height="100px"></a>
   <a href="http://www.ceico.cz/"><img src="https://academicpositions.eu/uploads/46e/083/46e083d07d2516e6b22c300bfe4731ac.jpeg" height="100px"></a>
   <a href="https://www.fzu.cz/"><img src="https://www.fzu.cz/sites/default/files/logo-FZU-velke_1000x600px.jpg" height="100px"></a>
