hour_str = input("what time is it now? ")
time_str = input("how many hours until alarm? ")

hour_int = int(hour_str)
time_int = int(time_str)

current_time = hour_int + time_int
alarm = current_time % 24

print("it is", alarm)
