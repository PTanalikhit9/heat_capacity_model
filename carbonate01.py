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
