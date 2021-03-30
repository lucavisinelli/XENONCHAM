# README

This repository contains the MontePython likelihood used in the paper to analyze the XENON1T data. This is a patch to the [Montepython3.3](https://github.com/brinckmann/montepython_public) cosmological MCMC sampler. If you want to use our code, you should therefore first of all download and install Montepython3.3 following the documentation provided. Even though we are using MontePython as a generic (i.e. non-cosmological sampler), you still need to give MontePython your path to CLASS in the usual default.conf file. Please refer to the general MontePython documentation for further information if you are unfamiliar with any of these steps. Here we'll just assume that you know how to run MontePython.

Once you have MontePython3.3 up and running, simply copy the content of the [montepython/likelihoods/XENON1T](https://github.com/lucavisinelli/XENONCHAM/tree/main/montepython/montepython/likelihoods/XENON1T) folder in your Path_to_your_montepython/montepython/likelihoods/ folder, and similarly for the [data](https://github.com/lucavisinelli/XENONCHAM/tree/main/montepython/data) folder, whose contents you should copy in your Path_to_your_montepython/data folder.

Then, assuming you've done everything correctly, you're all set up for running your MCMC chains! For this we have supplied the example param file [XENON1T.param](https://github.com/lucavisinelli/XENONCHAM/blob/main/montepython/XENON1T.param). The 6 parameters have the following meanings: <br />
ge -> log10(beta_e), with beta_e the coupling to electrons <br />
gg -> log10(beta_gamma), with beta_gamma the coupling to photons <br />
logMe -> log10(M_e/keV), with M_e the electron disformal scale <br />
logMg -> log10(M_gamma/keV), with M_gamma the photon disformal scale <br />
gc -> log10(Lambda/keV), with Lambda the chameleon potential scale <br />
ncham -> n, with n the chameleon potential power-law <br />
