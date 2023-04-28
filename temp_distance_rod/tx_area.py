
import numpy as np
import matplotlib.pyplot as plt

# Read data from the text file
def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            distance, temp = map(float, line.strip().split())
            data.append((distance, temp))
    return data

# Calculate the area under the graph
def calculate_area_under_graph(data):
    area = 0
    for i in range(1, len(data)):
        distance1, temp1 = data[i - 1]
        distance2, temp2 = data[i]
        area += 0.5 * (distance2 - distance1) * (temp1 + temp2)
    return area

# Calculate the average
def calculate_average(area, data):
    domain_length = data[-1][0] - data[0][0]
    average = area / domain_length
    return average

# Plot the graph and area under the graph
def plot_graph_and_area(data, area):
    distances, temps = zip(*data)
    plt.plot(distances, temps, '-o', label='Temperature')

    for i in range(1, len(data)):
        distance1, temp1 = data[i - 1]
        distance2, temp2 = data[i]
        plt.fill_between([distance1, distance2], [temp1, temp2], color='gray', alpha=0.3)

    plt.xlabel("Distance")
    plt.ylabel("Temperature")
    plt.title(f"Area under graph: {area:.2f}")
    plt.legend()
    plt.show()

# Main function
def main():
    filename = "Tx.txt"
    data = read_data_from_file(filename)
    area = calculate_area_under_graph(data)
    average = calculate_average(area, data)

    print(f"Area under graph: {area}")
    print(f"Average: {average}")

    plot_graph_and_area(data, area)

if __name__ == "__main__":
    main()
