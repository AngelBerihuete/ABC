# import the desired packages

import numpy as np
import astroabc
import numpy as np

# multivariate gaussian; example of using MPI
cov = [[0.009,0.005], [0.005,0.1]]  # diagonal covariance

# define the distance metric
def dist_metric_ro(observed,simulated):
        '''Distance metric: rho'''
        return np.sum(np.abs(np.mean(simulated,axis=0) - np.mean(observed,axis=0)))
# define the simulation
def simulation(param,pool=None):
    cov = [[0.009,0.005], [0.005,0.1]]
    mean=param
    sym=np.random.multivariate_normal(mean, cov, 1000)
    return sym
# define the main function
def main():
    mean = [0.037, 0.57]
    data=np.random.multivariate_normal(mean, cov, 1000)
    model_sim=simulation
    sampler = astroabc.ABC_class(2,100,data,[0.7,0.02],20,prior,**prop)

    sampler.sample(model_sim) # Here we run the ABC algoritm



# Define the properties for the astroabc package



if __name__ == "__main__":

 
        prop={'tol_type':"exp","verbose":1,'adapt_t':True,'threshold':75,
        'pert_kernel':2,'variance_method':0, 'dfunc':dist_metric_ro, 'restart':"restart_abc.txt", 'outfile':"abc_mpi.txt",'mpi':True,'mp':False,'num_proc':4,
        'from_restart':False}
#######

prior =  [('uniform', [0., 1.]),('uniform', [0., 1.])] # Define the priors por the parameters to explore
main()

