
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

# Load experimental data from raw.txt
time_exp, temperature_exp = np.loadtxt('raw.txt', delimiter='\t', unpack=True)

# Fit function
def fit_function(t, T_0, A, B):
    return T_0 + 1 / A * np.log(1 + A / B * t)

# Initial guess values
initial_guess = (29, 0.01473, 12.93)

# Fit the experimental data
params, _ = curve_fit(fit_function, time_exp, temperature_exp, p0=initial_guess)
T_0, A, B = params

# Evaluate the fitted function
temperature_fit = fit_function(time_exp, T_0, A, B)

# Plot the results
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot experimental data as a scatter plot
ax1.scatter(time_exp, temperature_exp, marker ='x', color = 'darkblue', label='Experimental data')
# ax1.scatter(time_exp, temperature_exp, label='Experimental data', alpha=0.5)

# # Plot the simulation result
ax1.plot(time_data, temperature_data, label='Simulation result', linestyle='--', color='black')

# Plot the fitted curve with fitting constants displayed up to 4 significant figures
ax1.plot(time_exp, temperature_fit, label=f'Fitted curve:T = {T_0:.2f} + (1/{A:.3f}) * ln(1 + ({A:.3f}/{B:.2f}) * t)', linestyle='-.', color='blue')

ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("Temperature vs Time")
ax1.legend()
