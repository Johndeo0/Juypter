from matplotlib import pyplot as plt

years = [1950,1960, 1970, 1980, 1990, 2000, 2010]
gdp = [3002., 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.show()


Print('--------------------')


movies = ["Annie Hall", "Ben-Hur", "Casablance", "gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

plt.xticks(range(len(movies)), movies)

plt.show()

print("----------------------------------------")

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs,variance,   'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
plt.plot(xs, total_error,   'b:', label='total error')


plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("the Bias-Variance Tradeoff")

plt.show()

print("-------------------------------------")
print("scatter plot")


friends = [70,65,72,63,71,64,60,64,67]
minutes = [175, 170, 205, 120, 220, 130, 105,145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'f']

plt.scatter(friends,minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
    xy=(friend_count, minute_count),
    xytext=(5,-5),
    textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of Friends")

plt.ylabel("daily minutes spent on the site")

plt.show()

