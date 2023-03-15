
import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 150 / 1000  # mass of water in kg
C_p0 = 4186  # specific heat capacity of water at 25°C in J/(kg·K)
alpha = 0.1  # temperature-dependent coefficient in J/(kg·K²)
heater_power = 50  # heater power in watts
initial_temperature = 29  # initial temperature in °C
final_temperature = 85  # final temperature in °C
time_step = 1  # time step in seconds

# Model heat capacity as a function of temperature
def heat_capacity(T):
    return C_p0 + alpha * T

# Calculate temperature change based on energy input
def temperature_change(energy, mass, T):
    return energy / (mass * heat_capacity(T))

