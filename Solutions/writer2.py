import time, random

filename = "shared_file.txt"

for i in range(5):
    with open(filename, "a") as f:
        f.write(f"Writer2 line {i}\n")
    time.sleep(random.uniform(0.5, 1))  # random delay
