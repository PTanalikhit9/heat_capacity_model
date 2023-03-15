
import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 100 / 1000  # mass of water in kg
C_p = 4186  # specific heat capacity of water in J/(kg·K)
initial_temperature = 29  # initial temperature in °C
final_temperature = 85  # final temperature in °C
time_step = 1  # time step in seconds
V = 12  # voltage of the power supply in volts
initial_power = 40  # initial power in watts
R0 = V ** 2 / initial_power  # initial resistance in ohms
alpha_R = 0.02  # temperature coefficient of resistivity

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

# Plot the results
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(time_data, temperature_data)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("Temperature vs Time")

plt.tight_layout()
plt.show()

# Save the figure as a PNG file
plt.savefig('temperature_vs_time.png', dpi=300)
