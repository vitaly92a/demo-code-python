#!/usr/bin/env python3

from random import *

solar_system_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]      # Pluto doesn't recognized as planet of Solar System
planets_list = len(solar_system_planets) - 1                                                                # calculation of the list begins from 0

chosen_planet_id = randint(0, planets_list)                                                                 # using integer option of random module

chosen_planet_name = solar_system_planets[chosen_planet_id]
planet_of_the_day = ''.join(map(str, chosen_planet_name))                                                   # how to make list item output without brackets

print("Planet of the day: ", planet_of_the_day)                                                             # final output

"""
This code has been written independently: without using ChatGPT or any other AI-tool!
Purpose of writing code: self-practice and personal usage.
Author: Vitaly A.
Contact: https://vitaly92a.github.io
"""