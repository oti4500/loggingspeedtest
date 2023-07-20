import os
import time
from datetime import datetime

hostname = "1.1.1.1" # specify the hostname or IP address you want to ping
ping_command = "ping -c 1 " + hostname
log_file = "ping_log.txt" # specify the name of the log file

with open(log_file, "a") as f:
    try:
        while True:
            response = os.popen(ping_command).read()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if "1 received" in response:
                ping_time = response.split("time=")[1].split(" ")[0]
                log_entry = f"{timestamp}; Ping time: {ping_time} ms; Hostname: {hostname}\n"
                print(log_entry)
                f.write(log_entry)
            else:
                log_entry = f"{timestamp} | Request timed out for {hostname}\n"
                print(log_entry)
                f.write(log_entry)
            time.sleep(1) # wait for 1 second before pinging again
    except KeyboardInterrupt:
        print("Script interrupted by user")

