from datetime import datetime

start = input()
end = input()
start_time = datetime.strptime(start, "%H:%M")
end_time = datetime.strptime(end, "%H:%M")
time = end_time - start_time
time = time.total_seconds() / 3600
print(time)
