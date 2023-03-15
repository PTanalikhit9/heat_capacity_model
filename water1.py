
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

# Initialize lists to store time, temperature, and heat capacity data
time_data = [0]
temperature_data = [initial_temperature]
heat_capacity_data = [heat_capacity(initial_temperature)]

# Simulate heating process
current_temperature = initial_temperature
while current_temperature < final_temperature:
    energy_input = heater_power * time_step
    delta_temperature = temperature_change(energy_input, mass, current_temperature)
    current_temperature += delta_temperature

    time_data.append(time_data[-1] + time_step)
    temperature_data.append(current_temperature)
    heat_capacity_data.append(heat_capacity(current_temperature))

# Plot the results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.plot(time_data, temperature_data)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("Temperature vs Time")

ax2.plot(temperature_data, heat_capacity_data)
ax2.set_xlabel("Temperature (°C)")
ax2.set_ylabel("Specific Heat Capacity (J/kg·K)")
ax2.set_title("Specific Heat Capacity vs Temperature")

plt.tight_layout()
plt.show()

