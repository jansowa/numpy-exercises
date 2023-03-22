import numpy as np

arr = np.arange("2017-05-01", "2017-05-08", np.timedelta64(1, 'D'), dtype=np.datetime64)

weekdays_arr = (arr.view('int64') - 4) % 7
print(weekdays_arr)
print(np.where(weekdays_arr == 0))
print(arr[np.where(weekdays_arr == 0)])

print(np.busday_offset('2017-05', 0, roll='forward', weekmask='Mon'))