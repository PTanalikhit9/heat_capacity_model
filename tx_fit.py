
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad
from scipy.special import erf

# Read data from the text file
def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            distance, temp = map(float, line.strip().split())
            data.append((distance, temp))
    return data

# Skewed Gaussian function
def skewed_gaussian(x, a, x0, sigma, alpha):
    return a * np.exp(-((x - x0) / sigma)**2 / 2) * (1 + erf(alpha * (x - x0) / (sigma * np.sqrt(2))))

# Fit the data with a skewed Gaussian function
def fit_skewed_gaussian(data):
    distances, temps = zip(*data)
    initial_guess = [max(temps), np.mean(distances), np.std(distances), 0]  # Initial guess for the parameters
    popt, pcov = curve_fit(skewed_gaussian, distances, temps, p0=initial_guess)
    return popt

# Integrate the skewed Gaussian function
def integrate_skewed_gaussian(popt, data):
    a, x0, sigma, alpha = popt
    integral, _ = quad(lambda x: skewed_gaussian(x, a, x0, sigma, alpha), data[0][0], data[-1][0])
    return integral

# Plot the scatter plot of the data and the fitting curve
def plot_data_and_fitting_curve(data, popt):
    distances, temps = zip(*data)
    x = np.linspace(data[0][0], data[-1][0], 1000)
    y = skewed_gaussian(x, *popt)
    
    plt.scatter(distances, temps, label='Data', color='r', marker='o')
    plt.plot(x, y, label='Fitting curve', color='b')
    plt.xlabel("Distance")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()

# Main function
def main():
    filename = "Tx.txt"
    data = read_data_from_file(filename)

    # Fit the data with a skewed Gaussian function
    popt = fit_skewed_gaussian(data)
    print(f"Fitted parameters (a, x0, sigma, alpha): {popt}")

    # Integrate the skewed Gaussian function and divide by the range of data
    integral = integrate_skewed_gaussian(popt, data)
    average = integral / (data[-1][0] - data[0][0])
    print(f"Integration result: {integral}")
    print(f"Average: {average}")

    # Plot the data and fitting curve
    plot_data_and_fitting_curve(data, popt)

if __name__ == "__main__":
    main()
