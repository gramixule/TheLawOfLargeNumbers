import random
import matplotlib.pyplot as plt


def generate_random_values(n, range_start, range_end):
    return [random.uniform(range_start, range_end) for _ in range(n)]


def calculate_mean(values):
    return sum(values) / len(values)


def plot_mean_vs_sample_size(n_values, range_start, range_end):
    means = []
    for i in range(1, n_values + 1):
        values = generate_random_values(i, range_start, range_end)
        mean = calculate_mean(values)
        means.append(mean)
    plt.plot(range(1, n_values + 1), means)
    plt.xlabel("Number of values")
    plt.ylabel("Mean")
    plt.show()


plot_mean_vs_sample_size(n_values=1000, range_start=0, range_end=1)
