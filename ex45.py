import numpy as np

all_numbers = np.arange(1, 1000)
print("All one, two and three digit numbers ", str(all_numbers))

each_type = np.array([np.random.randint(1, 10), np.random.randint(10, 100), np.random.randint(100, 1000)])
print("Single number of each type (one, two and three digits): ", str(each_type))

random_numbers = np.random.randint(1, 1000, size=np.random.randint(10, 20))
print("Some random numbers with one, two or three digits: ", str(random_numbers))