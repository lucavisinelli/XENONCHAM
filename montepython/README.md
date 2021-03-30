This repository contains the MontePython likelihood used in the paper to analyze the XENON1T data. This is a patch to the [Montepython3.3](https://github.com/brinckmann/montepython_public) cosmological MCMC sampler. If you want to use our code, you should therefore first of all download and install Montepython3.3 following the documentation provided. Even though we are using MontePython as a generic (i.e. non-cosmological sampler), you still need to give MontePython your path to CLASS in the usual default.conf file. Please refer to the general MontePython documentation for further information if you are unfamiliar with any of these steps. Here we'll just assume that you know how to run MontePython.