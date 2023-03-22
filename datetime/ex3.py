import numpy as np

print("Number of days, February, 2016:")
print(np.arange("2016-02", "2016-03", np.timedelta64(1, 'D'), dtype=np.datetime64).size)
print("Number of days, February, 2017:")
print(np.arange("2017-02", "2017-03", np.timedelta64(1, 'D'), dtype=np.datetime64).size)
print("Number of days, February, 2018:")
print(np.arange("2018-02", "2018-03", np.timedelta64(1, 'D'), dtype=np.datetime64).size)

print("Number of days, February, 2016:")
print(np.datetime64("2016-03-01") - np.datetime64("2016-02-01"))
print("Number of days, February, 2017:")
print(np.datetime64("2017-03-01") - np.datetime64("2017-02-01"))
print("Number of days, February, 2018:")
print(np.datetime64("2018-03-01") - np.datetime64("2018-02-01"))
