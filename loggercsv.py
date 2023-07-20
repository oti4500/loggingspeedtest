import os
import time
import csv

# Create the CSV log file and write the header row
with open("internet_speed_log.csv", "w") as log_file:
    csv_writer = csv.writer(log_file)
    csv_writer.writerow(["Timestamp", "Ping", "Download", "Upload"])

while True:
    # Run the speedtest-cli command and save the output to a variable
    speedtest_output = os.popen("speedtest-cli --simple").read()
    # Parse the output to extract the ping, download, and upload values
    lines = speedtest_output.split("\n")
    ping_line = lines[0]
    download_line = lines[1]
    upload_line = lines[2]
    ping = ping_line.split(":")[1].strip()
    download = download_line.split(":")[1].strip()
    upload = upload_line.split(":")[1].strip()
    # Open the CSV log file in append mode
    with open("internet_speed_log.csv", "a") as log_file:
        csv_writer = csv.writer(log_file)
        # Write a new row to the CSV log file with the current timestamp, ping, download, and upload values
        csv_writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), ping, download, upload])
    # Sleep for 15 minutes before running the speedtest again
    time.sleep(2 * 60)

