import statistics

data = [34.5, 18.4, 25.2, 40.5, 25.7, 28.8]
label_mean = "Mean"
label_stdev = "Standard Deviation"

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print(label_mean, mean)
print(label_stdev, stdev)

