import csv

with open('internet_speed_log.txt', 'r') as txt_file, open('output.csv', 'w') as csv_file:
    reader = txt_file.readlines()
    writer = csv.writer(csv_file)
    writer.writerow(['Timestamp', 'Ping', 'Download', 'Upload'])
    i = 0
    while i < len(reader):
        line = reader[i].strip()
        if line.startswith('Ping'):
            ping = line.split()[1]
        elif line.startswith('Download'):
            download = line.split()[1]
        elif line.startswith('Upload'):
            upload = line.split()[1]
            writer.writerow([timestamp, ping, download, upload])
        else:
            timestamp = line
        i += 1
