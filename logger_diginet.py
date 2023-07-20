import os
import time

while True:
    # Run the speedtest-cli command and save the output to a variable
    speedtest_output = os.popen("./speedtest -s 31717").read()
    # Open the log file in append mode
    with open("internet_speed_log_diginet.txt", "a") as log_file:
        # Write the current timestamp and speedtest output to the log file
        log_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        log_file.write(speedtest_output + "\n")
    # Sleep for 15 minutes before running the speedtest again
    time.sleep(3 * 60)

