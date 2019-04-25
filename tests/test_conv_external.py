# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, Caleb Bell <Caleb.Andrew.Bell@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

from __future__ import division
from ht import *
import numpy as np
from numpy.testing import assert_allclose
import pytest

### Conv external

def test_Nu_cylinder_Zukauskas():
    Nu = Nu_cylinder_Zukauskas(7992, 0.707, 0.69)
    assert_allclose(Nu, 50.523612661934386)

    Nus_allRe = [Nu_cylinder_Zukauskas(Re, 0.707, 0.69) for Re in np.logspace(0, 6, 8)]
    Nus_allRe_values = [0.66372630070423799, 1.4616593536687801, 3.2481853039940831, 8.7138930573143227, 26.244842388228189, 85.768869004450067, 280.29503021904566, 1065.9610995854582]
    assert_allclose(Nus_allRe, Nus_allRe_values)

    Nu_highPr = Nu_cylinder_Zukauskas(7992, 42.)
    assert_allclose(Nu_highPr, 219.24837219760443)



def test_Nu_cylinder_Churchill_Bernstein():
    Nu = Nu_cylinder_Churchill_Bernstein(6071, 0.7)
    assert_allclose(Nu, 40.63708594124974)


def test_Nu_cylinder_Sanitjai_Goldstein():
    Nu = Nu_cylinder_Sanitjai_Goldstein(6071, 0.7)
    assert_allclose(Nu, 40.38327083519522)


def test_Nu_cylinder_Fand():
    Nu = Nu_cylinder_Fand(6071, 0.7)
    assert_allclose(Nu, 45.19984325481126)


def test_Nu_cylinder_McAdams():
    Nu = Nu_cylinder_McAdams(6071, 0.7)
    assert_allclose(Nu, 46.98179235867934)


def test_Nu_cylinder_Whitaker():
    Nu = Nu_cylinder_Whitaker(6071, 0.7)
    assert_allclose(Nu, 45.94527461589126)
    Nu = Nu_cylinder_Whitaker(6071, 0.7, 1E-3, 1.2E-3)
    assert_allclose(Nu, 43.89808146760356)


def test_Nu_cylinder_Perkins_Leppert_1962():
    Nu = Nu_cylinder_Perkins_Leppert_1962(6071, 0.7)
    assert_allclose(Nu, 49.97164291175499)
    Nu = Nu_cylinder_Perkins_Leppert_1962(6071, 0.7, 1E-3, 1.2E-3)
    assert_allclose(Nu, 47.74504603464674)


def test_Nu_cylinder_Perkins_Leppert_1964():
    Nu = Nu_cylinder_Perkins_Leppert_1964(6071, 0.7)
    assert_allclose(Nu, 53.61767038619986)
    Nu = Nu_cylinder_Perkins_Leppert_1964(6071, 0.7, 1E-3, 1.2E-3)
    assert_allclose(Nu, 51.22861670528418)


def test_Nu_external_cylinder():
    Nu = Nu_external_cylinder(6071, 0.7)
    assert_allclose(Nu, 40.38327083519522)
    
    Nu = Nu_external_cylinder(6071, 0.7, Method='Zukauskas')
    assert_allclose(Nu, 42.4244052368103)
    
    methods = Nu_external_cylinder(6071, 0.7, AvailableMethods=True)
    
    with pytest.raises(Exception):
        Nu_external_cylinder(6071, 0.7, Method='BADMETHOD')


def test_Nu_horizontal_plate_laminar_Baehr():
    Prs = [1e-4, 1e-1, 1, 100]
    Nu_expects = [3.5670492006699317, 97.46187137010543, 209.9752366351804, 995.1679034477633]
    
    for Pr, Nu_expect in zip(Prs, Nu_expects):
        assert_allclose(Nu_horizontal_plate_laminar_Baehr(1e5, Pr), Nu_expect)


def test_Nu_horizontal_plate_laminar_Churchill_Ozoe():
    assert_allclose(Nu_horizontal_plate_laminar_Churchill_Ozoe(1e5, .7), 183.08600782591418)
    
    
def test_Nu_horizontal_plate_turbulent_Schlichting():
    assert_allclose(Nu_horizontal_plate_turbulent_Schlichting(1e5, 0.7), 309.620048541267)
    
    
def test_Nu_horizontal_plate_turbulent_Kreith():
    Nu = Nu_horizontal_plate_turbulent_Kreith(1.03e6, 0.71)
    assert_allclose(Nu, 2074.8740070411122)
    
    
def test_Nu_external_horizontal_plate():
    # default function - turbulent
    assert_allclose(Nu_external_horizontal_plate(5e6, .7),
                    Nu_external_horizontal_plate(5e6, .7, turbulent_method='Schlichting'))
    
    # specific function - turbulent - vs specify turbulent method
    assert_allclose(Nu_horizontal_plate_turbulent_Kreith(5e6, .7),
                    Nu_external_horizontal_plate(5e6, .7, turbulent_method='Kreith'))
    
    # specific function - turbulent - vs specify method
    assert_allclose(Nu_horizontal_plate_turbulent_Kreith(5e6, .7),
                    Nu_external_horizontal_plate(5e6, .7, Method='Kreith'))
    
    # default function - laminar
    assert_allclose(Nu_external_horizontal_plate(5e3, .7),
                    Nu_external_horizontal_plate(5e3, .7, laminar_method='Baehr'))
    
    # specific function - laminar - vs specify laminar method
    assert_allclose(Nu_horizontal_plate_laminar_Baehr(5e3, .7),
                    Nu_external_horizontal_plate(5e3, .7, laminar_method='Baehr'))
    
    # specific function - laminar - vs specify method
    assert_allclose(Nu_horizontal_plate_laminar_Churchill_Ozoe(5e6, .7),
                    Nu_external_horizontal_plate(5e6, .7, Method='Churchill Ozoe'))
    
    # Swith the transition region to be higher
    assert_allclose(Nu_horizontal_plate_laminar_Baehr(5e6, .7),
                    Nu_external_horizontal_plate(5e6, .7, Re_transition=1e7))
    
    # Check the AvailableMethods
    assert (set(Nu_external_horizontal_plate(1e5, .7, AvailableMethods=True)) 
            == set(conv_horizontal_plate_laminar_methods.keys()) )
    
    assert (set(Nu_external_horizontal_plate(1e7, .7, AvailableMethods=True)) 
            == set(conv_horizontal_plate_turbulent_methods.keys()) )