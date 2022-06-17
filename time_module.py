import time

# converts time in epoch to a date string
print(time.ctime(1000000))

# amount of seconds since epoch using computer clock
print(time.time())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_string = time.mktime(time_tuple)
print(time_string)