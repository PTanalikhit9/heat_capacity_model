import numpy as np
import matplotlib.pyplot as plt

def carbonate_water_temperature(t, T, Cp0, mc, Q, dt):
    Cp = Cp0 * np.exp(-0.01 * T) # Modeling the temperature dependence of specific heat capacity
    h = 0.1 * np.exp(-0.05 * t) # Modeling the time dependence of heat transfer coefficient
    dTdt = (Q - h * (T - 20)) / (mc * Cp)
    return T + dTdt * dt

dt = 0.1
t = np.linspace(0, 100, 1000)
T0 = 20
Cp0 = 4.18
mc = 0.5
Q = 200

temp = []
Cp_values = []

for i in range(len(t)):
    T = carbonate_water_temperature(t[i], T0, Cp0, mc, Q, dt)
    temp.append(T)
    Cp_values.append(Cp0 * np.exp(-0.01 * T))
    T0 = T

temp = np.array(temp)
Cp_values = np.array(Cp_values)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(t, temp)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Temperature (C)')
axs[0].set_title('Temperature vs Time')

axs[1].plot(temp, Cp_values)
axs[1].set_xlabel('Temperature (C)')
axs[1].set_ylabel('Specific Heat Capacity (J/kg.C)')
axs[1].set_title('Specific Heat Capacity vs Temperature')

axs[2].plot(t, Cp_values)
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Specific Heat Capacity (J/kg.C)')
axs[2].set_title('Specific Heat Capacity vs Time')

plt.show()
