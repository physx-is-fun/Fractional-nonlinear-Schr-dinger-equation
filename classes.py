from libraries import *
from variables import *

# Defining a class for the simulation parameters
# Class for holding info about the simulation params
class SIM_config:
    def __init__(self,N,time_window,duration,wavelength0):
        self.number_of_points=N
        self.wavelength0 = wavelength0                                             # Central wavelength
        self.duration = 1                                                          # Dimensonless duration
        dt = time_window / N
        self.time_step = dt / duration                                             # Dimensionless time step
        t = np.linspace(0,time_window,N)                                                                                  
        t = t - np.mean(t)
        self.t = t / duration                                                      # Dimensionless time grid
        f = fftshift(fftfreq(N,d=dt/duration))                                                                               
        self.f = f                                                                 
        frequency0 = speed_of_light / wavelength0                                  # Dimensionless central frequency
        self.frequency0 = 1                                                        # Dimensionless frequency grid
        f_rel = f + 1                                                                                      
        self.f_rel = f_rel                                                         # Dimensionless relative frequency grid

# Class for holding info about the fiber
class Fiber_config:
    def __init__(self,nsteps,length,nonlinear_length,dispersion_length,alpha_dB_per_m):
        self.nsteps=nsteps
        self.length = length
        dz = length / nsteps                                                       
        self.dz = dz / length                                                      # Dimensionless spatial step
        zlocs_array=np.linspace(0,length,nsteps)                                   
        self.zlocs_array = zlocs_array / length                                    # Dimensionless spatial grid                                   
        self.nonlinear_length = nonlinear_length
        self.dispersion_length = dispersion_length
        self.alpha_dB_per_m = alpha_dB_per_m 