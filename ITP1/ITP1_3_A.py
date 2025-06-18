import time

count = 1
start_time1 = time.time()
while count <= 1000:
    print("Hello World")
    count += 1
end_time1 = time.time() - start_time1


start_time2 = time.time()
for i in range(1000):
    print("Hello World")
end_time2 = time.time() - start_time2
print(f"while: {end_time1}")
print(f"for: {end_time2}")

