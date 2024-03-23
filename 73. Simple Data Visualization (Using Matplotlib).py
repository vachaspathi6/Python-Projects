import matplotlib.pyplot as plt

def plot_data(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Data Visualization')
    plt.show()

def main():
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]
    plot_data(x_values, y_values)

if __name__ == "__main__":
    main()
