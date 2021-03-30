from montepython.likelihood_class import Likelihood_prior
import numpy as np
from scipy import interpolate
import os

class XENON1T(Likelihood_prior):
    
    def __init__(self, path, data, command_line):

        Likelihood_prior.__init__(self, path, data, command_line)

    def loglkl(self, cosmo, data):

        hbar  = 6.582119569e-19
        cs    = 2.99792458e10
        hbarc = hbar*cs
        me    = 511.
        RSun  = 6.9634e10
        dSun  = 1.5e13
        mPl   = 1.221e25
        alpha = 1./137.036
        
        xt    = 0.7
        Bt    = 0.021
        rhot  = 891921.86598
        TSun  = 0.1995759863
        ne    = 1.06051586e+23
        lam   = 0.3
        ng    = 1.e21
        Dx    = 0.01
        
        pc    = 3.086e18
        gkeV  = 1.782662e-30
        year  = 3.15e7
        NXe   = 4.58644e21
        conv  = 10**6*year
        tXE   = 1.042e6

        pi2   = 2.*np.pi
        pi4   = 4.*np.pi
        pi8   = 8.*np.pi

        xd, yC = np.loadtxt(os.path.join(self.data_directory, self.central_file), unpack=True)
        xd, yL = np.loadtxt(os.path.join(self.data_directory, self.lower_file), unpack=True)
        xd, yU = np.loadtxt(os.path.join(self.data_directory, self.upper_file), unpack=True)
        enb, backb = np.loadtxt(os.path.join(self.data_directory, self.signal_file), unpack=True)
        ekeV, eff = np.loadtxt(os.path.join(self.data_directory, self.efficiency_file), unpack=True)
        EMeV, sigme = np.loadtxt(os.path.join(self.data_directory, self.photoe_file), unpack=True)

        yU=yU-yC
        yL=yC-yL
        sigDsym = (yU+yL)/2.
        sigD = np.array([yL,yU])
        back   = interpolate.interp1d(enb, backb, fill_value=(0.0, 0.0), bounds_error=False)
        epsilon   = interpolate.interp1d(ekeV, eff, fill_value=(0.,0.89), bounds_error=False)
        
        def res_sgm(omR, om):
            sgm = 0.31*np.sqrt(omR) + 0.0037*omR
            return np.exp(-0.5*(om-omR)**2/sgm**2)/np.sqrt(pi2)/sgm
        res_sgm = np.vectorize(res_sgm)
        
        omPl2 = pi4*alpha*ne*hbarc**3/me
        
        def mphi2(ge, gc, n):
            phim = (n*mPl*10**((4.+n)*gc-ge)/rhot)**(1./(1.+n))
            return (1.+n)*10**ge*rhot/mPl/phim
        
        def Int(a):
            return np.sqrt(np.pi/2.)*(np.sqrt(a + np.sqrt(a**2+4.)) - np.sqrt(2.*a))
        
        def bg2(logMg):
            return Bt**4/10**(8.*logMg)
        
        def DeltaB(gg, logMg):
            return 2.*10**gg*Bt/mPl/np.sqrt(1.+bg2(logMg) )
        
        def DeltaPl(om):
            return 0.5*omPl2/om

        def Delta_a(om, ge, gc, n, logMg):
            temp = mphi2(ge, gc, n)/2./om + bg2(logMg)*om*(2./3.)
            return temp/(1.+ bg2(logMg) )
        
        def DEN(om, ge, gg, gc, n, logMg):
            return 4.*DeltaB(gg, logMg)**2 + (DeltaPl(om) - Delta_a(om, ge, gc, n, logMg))**2

        def lom(om, ge, gg, gc, n, logMg):
            return 2.*hbarc/np.sqrt(DEN(om, ge, gg, gc, n, logMg))
        
        def pg(om):
            return om**2/TSun**3/(np.exp(om/TSun)-1.)/2.404
        
        def Pcham(om, ge, gg, gc, n, logMg):
            lo = lom(om, ge, gg, gc, n, logMg)
            dd = DEN(om, ge, gg, gc, n, logMg)
            return Dx*np.sqrt(cs/lo)*RSun/lam*4.*DeltaB(gg, logMg)**2/dd*Int(lo/lam)
        
        def dPhidomega_cham(om, ge, gg, gc, n, logMg):
            return ng*pg(om)*Pcham(om, ge, gg, gc, n, logMg)*(RSun/dSun)**2/4.
        
        def sigma_cham_dis(om, logMe):
            return 0.5*NXe*(hbarc*me*om**2/pi2/10**(4.*logMe))**2
        
        sigmae = interpolate.interp1d(EMeV*1.e3, sigme, fill_value=(sigme[0],0), bounds_error=False)
        
        def sigma_cham_abs(om, ge):
            return (10**ge*om/mPl)**2*sigmae(om)*4./alpha
        
        def sigma_cham(om, ge, logMe):
            return sigma_cham_dis(om, logMe) + sigma_cham_abs(om, ge)
        
        def Rate_bare_cham(om, ge, gg, gc, n, logMe, logMg):
            ret = 0
            if om > 0:
              ret = np.nan_to_num(conv*sigma_cham(om, ge, logMe)*dPhidomega_cham(om, ge, gg, gc, n, logMg))
            return ret
        Rate_bare_cham = np.vectorize(Rate_bare_cham)
        
        def Rate_cham(om, ge, gg, gc, n, logMe, logMg):
            omp = np.geomspace(0.01, 10.0, 100)
            omX = Rate_bare_cham(omp, ge, gg, gc, n, logMe, logMg)
            cnv = epsilon(om)*np.trapz(res_sgm(omp, om)*omX, omp)
            return cnv
        Rate_cham = np.vectorize(Rate_cham)
        
        backxd = back(xd)
        def chisq(ge, gg, gc, n, logMe, logMg):
            cnv_chisq = Rate_cham(xd, ge, gg, gc, n, logMe, logMg)
            cnv_chisq = cnv_chisq + backxd
            mychisq = 0.0
            for i in range(1,4):
                mychisq = mychisq + ((cnv_chisq[i]-yC[i])/sigDsym[i])**(2.0)
            return mychisq

        ge_mcmc = data.mcmc_parameters['ge']['current']*data.mcmc_parameters['ge']['scale']
        gg_mcmc = data.mcmc_parameters['gg']['current']*data.mcmc_parameters['gg']['scale']
        gc_mcmc = data.mcmc_parameters['gc']['current']*data.mcmc_parameters['gc']['scale']
        ncham_mcmc = data.mcmc_parameters['ncham']['current']*data.mcmc_parameters['ncham']['scale']
        logMe_mcmc = data.mcmc_parameters['logMe']['current']*data.mcmc_parameters['logMe']['scale']
        logMg_mcmc = data.mcmc_parameters['logMg']['current']*data.mcmc_parameters['logMg']['scale']

        loglkl = -0.5 * chisq(ge_mcmc, gg_mcmc, gc_mcmc, ncham_mcmc, logMe_mcmc, logMg_mcmc)

        return loglkl
