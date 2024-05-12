import numpy
import scipy
import statistics

numbers_list = [10, 20, 30, 50, 10, 80, 90, 10, 70]
print(f"Data : {numbers_list}")

mean_of_numbers = numpy.mean(numbers_list)
print(f"Mean : {mean_of_numbers}")

median_of_numbers = numpy.median(numbers_list)
print(f"Median : {median_of_numbers}")

mode_of_numbers = statistics.mode(numbers_list)
print(f"Mode : {mode_of_numbers}")

standard_deviation_of_numbers = numpy.std(numbers_list)
print(f"Standard Deviation : {standard_deviation_of_numbers}")

variance_of_numbers = numpy.var(numbers_list)
print(f"Variance : {variance_of_numbers}")
