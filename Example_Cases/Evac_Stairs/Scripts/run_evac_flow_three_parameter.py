#!/usr/bin/env python

"""
PyMC Bayesian Inference on Evacuation Data
Model 1: Pre-Evacuation Intensity
Model 2: Travel Intensity
Model 3: Exit Intensity
"""

import matplotlib
matplotlib.use("Agg")

import pylab as pl
import evac_flow_three_parameter_graphics as graphics
import pymc as mc
import evac_flow_three_parameter_models as models
import data_evac

#  ============
#  = Settings =
#  ============

mcmc_iterations = 1000000
burn_iterations = 800000
thinning_parameter = 200

case_name = 'three_parameter'

#  ===========
#  = Model 1 =
#  ===========

# Generate model
vars1 = models.model1()

# Fit model with MAP estimates
map = mc.MAP(vars1)
map.fit(method='fmin_powell', verbose=2)

# Import model variables and set database options
m1 = mc.MCMC(vars1, db='sqlite', dbname='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model1.sqlite')

# Use adaptive Metropolis-Hastings step method
m1.use_step_method(mc.AdaptiveMetropolis, [m1.theta])

# Configure and run MCMC simulation
m1.sample(iter=mcmc_iterations, burn=burn_iterations, thin=thinning_parameter)

# Plot traces and model with mean values
# pl.figure(figsize=(12,9))
# graphics.plot_evac_data()
# graphics.plot_model1(m1)
# pl.savefig('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model1.pdf')

# Plot resulting distributions and convergence diagnostics
mc.Matplot.plot(m1, format='pdf', path='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model1',
                common_scale=False)

#  ===========
#  = Model 2 =
#  ===========

# Generate model
vars2 = models.model2()

# Fit model with MAP estimates
map = mc.MAP(vars2)
map.fit(method='fmin_powell', verbose=2)

# Import model variables and set database options
m2 = mc.MCMC(vars2, db='sqlite', dbname='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model2.sqlite')

# Use adaptive Metropolis-Hastings step method
m2.use_step_method(mc.AdaptiveMetropolis, [m2.theta])

# Configure and run MCMC simulation
m2.sample(iter=mcmc_iterations, burn=burn_iterations, thin=thinning_parameter)

# Plot traces and model with mean values
# pl.figure(figsize=(12,9))
# graphics.plot_evac_data()
# graphics.plot_model2(m2)
# pl.savefig('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model2.pdf')

# Plot resulting distributions and convergence diagnostics
mc.Matplot.plot(m2, format='pdf', path='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model2',
                common_scale=False)

#  ===========
#  = Model 3 =
#  ===========

# Generate model
vars3 = models.model3()

# Fit model with MAP estimates
map = mc.MAP(vars3)
map.fit(method='fmin_powell', verbose=2)

# Import model variables and set database options
m3 = mc.MCMC(vars3, db='sqlite', dbname='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model3.sqlite')

# Use adaptive Metropolis-Hastings step method
m3.use_step_method(mc.AdaptiveMetropolis, [m3.theta])

# Configure and run MCMC simulation
m3.sample(iter=mcmc_iterations, burn=burn_iterations, thin=thinning_parameter)

# Plot traces and model with mean values
# pl.figure(figsize=(12,9))
# graphics.plot_evac_data()
# graphics.plot_model3(m3)
# pl.savefig('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model3.pdf')

# Plot resulting distributions and convergence diagnostics
mc.Matplot.plot(m3, format='pdf', path='../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model3',
                common_scale=False)

#  =================
#  = Print results =
#  =================

# Display results
print "Results for Model 1 - Pre-Evacuation Intensity"
m1.theta.summary()
print "Results for Model 2 - Travel Intensity"
m2.theta.summary()
print "Results for Model 3 - Exit Intensity"
m3.theta.summary()

# Write results to file
m1.write_csv('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model1.csv')
m2.write_csv('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model2.csv')
m3.write_csv('../Figures/Three_Parameter_Models/flow_' + case_name + '_evac_model3.csv')

# Find DIC
print 'DIC (Model 1) = %f' % m1.dic
print 'DIC (Model 2) = %f' % m2.dic
print 'DIC (Model 3) = %f' % m3.dic
