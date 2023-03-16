import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##############################################################

# Constants
mass = 100 / 1000  # mass of water in kg
C_p = 4186  # specific heat capacity of water in J/(kg·K)
initial_temperature = 29  # initial temperature in °C
final_temperature = 85  # final temperature in °C
time_step = 1  # time step in seconds
V = 12  # voltage of the power supply in volts
initial_power = 40  # initial power in watts
R0 = V ** 2 / initial_power  # initial resistance in ohms
alpha_R = 0.0317  # temperature coefficient of resistivity note: 0.03

# Initialize lists to store time, temperature, and power data
time_data = [0]
temperature_data = [initial_temperature]
power_data = [initial_power]

# Calculate temperature change based on the energy input and heat capacity
def temperature_change(energy_input, mass, C_p):
    return energy_input / (mass * C_p)

# Simulate heating process
current_temperature = initial_temperature
while current_temperature < final_temperature:
    R = R0 * (1 + alpha_R * (current_temperature - initial_temperature))
    power = V ** 2 / R
    energy_input = power * time_step
    delta_temperature = temperature_change(energy_input, mass, C_p)
    current_temperature += delta_temperature

    time_data.append(time_data[-1] + time_step)
    temperature_data.append(current_temperature)
    power_data.append(power)

##############################################################
