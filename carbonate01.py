import numpy as np
import matplotlib.pyplot as plt

def carbonate_water_temperature(t, T, Cp0, mc, Q, dt):
    Cp = Cp0 * np.exp(-0.01 * T) # Modeling the temperature dependence of specific heat capacity
    h = 0.1 * np.exp(-0.05 * t) # Modeling the time dependence of heat transfer coefficient
    dTdt = (Q - h * (T - 20)) / (mc * Cp)
    return T + dTdt * dt
