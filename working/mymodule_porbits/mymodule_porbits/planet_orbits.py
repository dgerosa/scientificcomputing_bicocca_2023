from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib as mp
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

mp.rc('text', usetex=True)
mp.rcParams['axes.labelsize']  = 20
mp.rcParams['axes.titlesize']  = 20
mp.rcParams['xtick.labelsize'] = 18
mp.rcParams['ytick.labelsize'] = 18


def rhs(t, x):
    r = np.sqrt(x[0]**2+x[1]**2)
    xdot = x[2]
    ydot = x[3]
    vxdot = - 4*np.pi**2*x[0]/r**3
    vydot =  - 4*np.pi**2*x[1]/r**3
    
    return np.array([xdot, ydot, vxdot, vydot])


def ode_integrate(X0, dt, tmax):

    #evolve it from a time 0 to tmax
    r = integrate.solve_ivp(rhs, (0.0, tmax), X0, method="RK45", dense_output=True, rtol=1e-10, atol=1.e-10)

    #get the solution at intermediate times
    ts = np.arange(0.0, tmax, dt)

    Xs = r.sol(ts)

    return ts, Xs

    
def planet_orbits():
    
    """
    Create the solar system planet orbits figure
    """
    
    #eccentrities and semimajor axis for all the planets
    e = np.array([0.2056, 0.0067, 0.016, 0.0934, 0.049, 0.056, 0.046, 0.010])
    a = np.array([0.387, 0.723, 1.016, 1.666, 5.458, 10.123, 20.02, 30.05])

    #initial condition
    X0 = np.array( [a*(1-e), np.zeros(8), np.zeros(8), np.sqrt(4*np.pi**2/a*(1+e)/(1+e))] )

    tmax = np.array([0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.79])
    dt = 0.01

    time = []
    X = []

    for i in range(8):
        t, x = ode_integrate(X0[:,i], dt, tmax[i])
        time.append(t)
        X.append(x)



    #-------------------------------- 
    # Plot the orbits of the planets 
    #-------------------------------- 
    fig, ax = plt.subplots(figsize=(12,9))

    #dictionary with planets and colors
    planet_colors = {
        r'$\rm Mercury$': 'gray',
        r'$\rm Venus$': 'goldenrod',
        r'$\rm Earth$': 'mediumblue',
        r'$\rm Mars$': 'red',
        r'$\rm Jupiter$': 'orange',
        r'$\rm Saturn$': 'gold',
        r'$\rm Uranus$': 'lightblue',
        r'$\rm Neptune$': 'darkblue',
    }

    for planet, color in planet_colors.items():
        pindex = list(planet_colors.keys()).index(planet)
        ax.plot(X[pindex][0, :], X[pindex][1, :], color=color, label=planet, ls='solid')
        if pindex>=4:
            ax.text(X[pindex][0, int(len(time[pindex])/2)]+0.1, X[pindex][1, int(len(time[pindex])/2)], planet)

    ax.plot(0,0, 'o', markersize=1, color='orange')
    ax.tick_params(axis="both", which='major', width=1, length=4, labelsize= 15, direction='in')  
    ax.xaxis.set_major_locator(MultipleLocator(10)) 
    ax.yaxis.set_major_locator(MultipleLocator(10)) 
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.set_title(r'$\rm Solar\,system:\,planet\,orbits$')
    ax.set_xlabel(r'$x \rm \, [UA]$', fontsize = 15)
    ax.set_ylabel(r'$y \rm \, [UA]$', fontsize = 15)
    ax.set_xlim(-32,32)
    ax.set_ylim(-32,32)

    inset_axes = plt.axes([0.6, 0.6, 0.3, 0.28])

    for planet, color in planet_colors.items():
        pindex = list(planet_colors.keys()).index(planet)
        if pindex<=3:
            inset_axes.plot(X[pindex][0, :], X[pindex][1, :], color=color, label=planet, ls='solid')
            inset_axes.text(X[pindex][0, int(len(time[pindex])/3)]-0.05, X[pindex][1, int(len(time[pindex])/3)]-0.15, planet)

    inset_axes.plot(0,0, 'o', markersize=5, color='orange')
    inset_axes.set_xlim(-1.5,1.5)
    inset_axes.set_ylim(-1.5,1.5)
    inset_axes.tick_params(axis="both", which='major', width=1, length=4, labelsize= 15, direction='in')  
    inset_axes.xaxis.set_major_locator(MultipleLocator(1)) 
    inset_axes.yaxis.set_major_locator(MultipleLocator(1)) 
    inset_axes.yaxis.set_ticks_position('both')
    inset_axes.xaxis.set_ticks_position('both')
    
    return fig