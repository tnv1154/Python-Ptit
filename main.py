from datetime import datetime

start = input()
end = input()
start_time = datetime.strptime(start, "%d/%m/%Y")
end_time = datetime.strptime(end, "%d/%m/%Y")

time = end_time - start_time
time = time.total_seconds() / (60 * 60 * 24)
print(time)
