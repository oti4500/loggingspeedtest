import os
import time

def log_traceroute(hostname):
    while True:
        try:
            with open("traceroute.log", "a") as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.write(os.popen("traceroute " + hostname).read() + "\n")
            time.sleep(60)
        except KeyboardInterrupt:
            print("Program interrupted by user.")
            break

log_traceroute("index.hu")

