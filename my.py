import datetime
import random
import matplotlib.pyplot as plt

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def calculate_standard_deviation(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

# Generate 500 random numbers in the range [-20, 20]
random_numbers = [random.uniform(-20, 20) for _ in range(500)]

# Calculate mean, median, and standard deviation
mean_value = calculate_mean(random_numbers)
median_value = calculate_median(random_numbers)
standard_deviation_value = calculate_standard_deviation(random_numbers, mean_value)

print("the random numbers generated are:", random_numbers)
print("The Mean is :", mean_value)
print("The Median is:", median_value)
print("The Standard Deviation is:", standard_deviation_value)

# Plot the histogram with 10 bins and customize appearance
plt.hist(random_numbers, bins=10, edgecolor='black', color='blue', alpha=0.7)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of 500 Random Numbers', fontsize=14)
plt.axvline(mean_value, color='black', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='red', linestyle='dashed', linewidth=2, label=f'Median: {median_value:.2f}')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")
