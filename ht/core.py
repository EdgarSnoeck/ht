# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, 2017, 2018 Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from __future__ import division
from math import log

__all__ =['LMTD', 'wall_factor', 'is_heating_property', 
'is_heating_temperature', 'wall_factor_fd', 'wall_factor_Nu',
'Kays_Crawford_turbulent_gas_Nu',
'Kays_Crawford_turbulent_gas_fd',
'Kays_Crawford_turbulent_liquid_Nu',
'Kays_Crawford_turbulent_liquid_fd',
'Kays_Crawford_laminar_gas_Nu',
'Kays_Crawford_laminar_gas_fd',
'Kays_Crawford_laminar_liquid_fd',
'Kays_Crawford_laminar_liquid_Nu']

def LMTD(Thi, Tho, Tci, Tco, counterflow=True):
    r'''Returns the log-mean temperature difference of an ideal counterflow
    or co-current heat exchanger.

    .. math::
        \Delta T_{LMTD}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)}

        \text{For countercurrent:      } \\
        \Delta T_1=T_{h,i}-T_{c,o}\\
        \Delta T_2=T_{h,o}-T_{c,i}

        \text{Parallel Flow Only:} \\
        {\Delta T_1=T_{h,i}-T_{c,i}}\\
        {\Delta T_2=T_{h,o}-T_{c,o}}

    Parameters
    ----------
    Thi : float
        Inlet temperature of hot fluid, [K]
    Tho : float
        Outlet temperature of hot fluid, [K]
    Tci : float
        Inlet temperature of cold fluid, [K]
    Tco : float
        Outlet temperature of cold fluid, [K]
    counterflow : bool, optional
        Whether the exchanger is counterflow or co-current

    Returns
    -------
    LMTD : float
        Log-mean temperature difference [K]

    Notes
    -----
    Any consistent set of units produces a consistent output.

    Examples
    --------
    Example 11.1 in [1]_.

    >>> LMTD(100., 60., 30., 40.2)
    43.200409294131525
    >>> LMTD(100., 60., 30., 40.2, counterflow=False)
    39.75251118049003

    References
    ----------
    .. [1] Bergman, Theodore L., Adrienne S. Lavine, Frank P. Incropera, and
       David P. DeWitt. Introduction to Heat Transfer. 6E. Hoboken, NJ:
       Wiley, 2011.
    '''
    if counterflow:
        dTF1 = Thi-Tco
        dTF2 = Tho-Tci
    else:
        dTF1 = Thi-Tci
        dTF2 = Tho-Tco
    return (dTF2 - dTF1)/log(dTF2/dTF1)


def is_heating_temperature(T, T_wall):
    r'''Checks whether or not a fluid side is being heated or cooled, from
    the temperature of the wall and the bulk temperature. Returns True for
    heating the bulk fluid, and False for cooling the bulk fluid.

    Parameters
    ----------
    T : float
        Temperature of flowing fluid away from the heat transfer surface, [K]
    T_wall : float
        Temperature of the fluid at the wall, [K]

    Returns
    -------
    is_heating : bool
        Whether or not the flow is being heated up by the wall, [-]

    Examples
    --------
    >>> is_heating_temperature(298.15, 350)
    True
    '''
    return T_wall > T

def is_heating_property(prop, prop_wall):
    r'''Checks whether or not a fluid side is being heated or cooled, from
    a property of the fluid at the wall and the bulk temperature. Returns True 
    for heating the bulk fluid, and False for cooling the bulk fluid.
    
    Parameters
    ----------
    prop : float
        Viscosity (or Prandtl number) of flowing fluid away from the heat
        transfer surface, [Pa*s]
    prop_wall : float
        Viscosity (or Prandtl number) of the fluid at the wall, [Pa*s]

    Returns
    -------
    is_heating : bool
        Whether or not the flow is being heated up by the wall, [-]

    Examples
    --------
    >>> is_heating_property(1E-3, 1.2E-3)
    False
    '''
    return prop_wall < prop


WALL_FACTOR_VISCOSITY = 'Viscosity'
WALL_FACTOR_PRANDTL = 'Prandtl'
WALL_FACTOR_TEMPERATURE = 'Temperature'
WALL_FACTOR_DEFAULT = 'Default'

# All powers were originally for (wall/bulk)^power, but have been negated here.

# Results for Deissler
# -0.11 is also an option from another presented correlation
Kays_Crawford_laminar_liquid_Nu = {'mu_heating_coeff': 0.14, 
                                   'mu_cooling_coeff': 0.14,
                                   'property_option': WALL_FACTOR_VISCOSITY}

Kays_Crawford_laminar_liquid_fd = {'mu_heating_coeff': -0.58, 
                                   'mu_cooling_coeff': -0.5,
                                   'property_option': WALL_FACTOR_VISCOSITY}

# 1.35 as a result suggested by an experiment byt the analysis is "prefered"
Kays_Crawford_laminar_gas_fd = {'mu_heating_coeff': -1, 
                                'mu_cooling_coeff': -1,
                                'property_option': WALL_FACTOR_VISCOSITY}
# This is uncertain
Kays_Crawford_laminar_gas_Nu = {'mu_heating_coeff': 0.0, 
                                'mu_cooling_coeff': 0.0,
                                'property_option': WALL_FACTOR_VISCOSITY}

# These seem fairly well measured
Kays_Crawford_turbulent_liquid_fd = {'mu_heating_coeff': -0.25, 
                                     'mu_cooling_coeff': -0.25,
                                     'property_option': WALL_FACTOR_VISCOSITY}
# This is uncertain
Kays_Crawford_turbulent_liquid_Nu = {'mu_heating_coeff': 0.11, 
                                     'mu_cooling_coeff': 0.25,
                                     'property_option': WALL_FACTOR_VISCOSITY}

# These see pretty accurate
Kays_Crawford_turbulent_gas_fd = {'mu_heating_coeff': 0.1, 
                                  'mu_cooling_coeff': 0.1,
                                  'property_option': WALL_FACTOR_VISCOSITY}

Kays_Crawford_turbulent_gas_Nu = {'mu_heating_coeff': 0.5, 
                                  'mu_cooling_coeff': 0.0,
                                  'property_option': WALL_FACTOR_VISCOSITY}


# is_turbulent, is_liquid
wall_factor_fd_defaults = {(True, True): Kays_Crawford_turbulent_liquid_fd,
                           (True, False): Kays_Crawford_turbulent_gas_fd,
                           (False, True): Kays_Crawford_laminar_liquid_fd,
                           (False, False): Kays_Crawford_laminar_gas_fd}
    
wall_factor_Nu_defaults = {(True, True): Kays_Crawford_turbulent_liquid_Nu,
                           (True, False): Kays_Crawford_turbulent_gas_Nu,
                           (False, True): Kays_Crawford_laminar_liquid_Nu,
                           (False, False): Kays_Crawford_laminar_gas_Nu}


def wall_factor_fd(mu, mu_wall, turbulent=True, liquid=False):
    params = wall_factor_fd_defaults[(turbulent, liquid)]
    return wall_factor(mu=mu, mu_wall=mu_wall, **params)


def wall_factor_Nu(mu, mu_wall, turbulent=True, liquid=False):
    r'''Computes the wall correction factor for heat transfer between a fluid
    and a wall. These coefficients were derived for internal flow inside a 
    pipe, but can be used elsewhere where appropriate data is missing. It is
    also useful to compare these results with the coefficients used in various
    heat transfer coefficients.
    
    .. math::
        \frac{Nu}{Nu_{\text{constant properties}}} 
        = \left(\frac{Pr}{Pr_{wall}}\right)^n

    Parameters
    ----------
    mu : float
        Viscosity (or Prandtl number) of flowing fluid away from the heat
        transfer surface, [Pa*s]
    mu_wall : float
        Viscosity (or Prandtl number) of the fluid at the wall, [Pa*s]
    turbulent : bool
        Whether or not to use the turbulent coefficient, [-]
    liquid : bool
        Whether or not to use the liquid phase coefficient; otherwise the gas
        coefficient is used, [-]
        
    Returns
    -------
    factor : float
        Correction factor for heat transfer; to be multiplied by the Nusselt
        number, or heat transfer coefficient to obtain the actual result, [-]

    Examples
    --------
    >>> wall_factor_Nu(mu=8E-4, mu_wall=3E-4, turbulent=True, liquid=True)
    1.1139265634480144
    
    >>> wall_factor_Nu(mu=8E-4, mu_wall=3E-4, turbulent=False, liquid=True)
    1.147190712947014
    
    >>> wall_factor_Nu(mu=1.5E-5, mu_wall=1.3E-5, turbulent=True, liquid=False)
    1.0741723110591495
    
    >>> wall_factor_Nu(mu=1.5E-5, mu_wall=1.3E-5, turbulent=False, liquid=False)
    1.0

    References
    ----------
    .. [1] Kays, William M., and Michael E. Crawford. Convective Heat and Mass 
       Transfer. 3rd edition. New York: McGraw-Hill Science/Engineering/Math,
       1993.
    '''
    params = wall_factor_Nu_defaults[(turbulent, liquid)]
    return wall_factor(mu=mu, mu_wall=mu_wall, **params)


def wall_factor(mu=None, mu_wall=None, Pr=None, Pr_wall=None, T=None, 
                T_wall=None, mu_heating_coeff=0.11, Pr_heating_coeff=0.11, 
                T_heating_coeff=0.11, mu_cooling_coeff=0.25, 
                Pr_cooling_coeff=0.25, T_cooling_coeff=0.25,
                property_option=WALL_FACTOR_PRANDTL):
    if property_option == WALL_FACTOR_DEFAULT:
        property_option = WALL_FACTOR_PRANDTL
    if property_option == WALL_FACTOR_VISCOSITY:
        if mu is None or mu_wall is None:
            raise TypeError('Viscosity wall correction specified but both '
                            'viscosity values are not available.')
        heating = is_heating_property(mu, mu_wall)
        if heating:
            return (mu/mu_wall)**mu_heating_coeff
        else:
            return (mu/mu_wall)**mu_cooling_coeff
    elif property_option == WALL_FACTOR_TEMPERATURE: 
        if T is None or T_wall is None:
            raise TypeError('Temperature wall correction specified but both '
                            'temperature values are not available.')
        heating = is_heating_temperature(T, T_wall)
        if heating:
            return (T/T_wall)**T_heating_coeff
        else:
            return (T/T_wall)**T_cooling_coeff
    elif property_option == WALL_FACTOR_PRANDTL: 
        if Pr is None or Pr_wall is None:
            raise TypeError('Prandtl number wall correction specified but both'
                            ' Prandtl number values are not available.') 
        heating = is_heating_property(Pr, Pr_wall)
        if heating:
            return (Pr/Pr_wall)**Pr_heating_coeff
        else:
            return (Pr/Pr_wall)**Pr_cooling_coeff
    else:
        raise Exception('Supported options are %s' %([WALL_FACTOR_VISCOSITY, 
                                                      WALL_FACTOR_PRANDTL, 
                                                      WALL_FACTOR_TEMPERATURE,
                                                      WALL_FACTOR_DEFAULT]))

