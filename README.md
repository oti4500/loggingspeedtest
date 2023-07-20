# loggingspeedtest
Speedtest logger to professional internet connectivity testing and results logging purpose.

Using logger.py

Requirements:
Python3 and PIP(3), speedtest-cli

Install speedtest-cli with pip(3)

Start the logger.py program and logging the speedtest results (using "nearby" servers). (in linux: sudo python3 logger.py)

Example from internet_speed_log.txt:
2023-07-20 04:26:38
Ping: 9.836 ms
Download: 907.06 Mbit/s
Upload: 303.55 Mbit/s

---

Using logger_nearest_server.py and logger_diginet.py

Python3 and Speedtest CLI program (from: https://www.speedtest.net/apps/cli)

If you use linux, extract to loggingspeedtest (or kind of) folder (where included the logger_nearest_server.py and will the internet_speed_log_nearestserver.txt)

If you fistly use the Speedtest CLI, you must have running the ./speedtest from directory and accept the EULA. After you can use logger_nearest_server.py (in linux: logger_nearest_server.py)

In log include all information by the Speedtest

Logging example from internet_speed_log_nearestserver.txt: 

2023-07-20 09:54:31

   Speedtest by Ookla

      Server: Digi Kft - Budapest (id: 31717)
         ISP: Digi TV
Idle Latency:     5.86 ms   (jitter: 0.45ms, low: 5.07ms, high: 6.08ms)

    Download:   694.46 Mbps (data used: 1.3 GB)                                                   
                 15.06 ms   (jitter: 2.42ms, low: 5.18ms, high: 224.52ms)

      Upload:   310.34 Mbps (data used: 484.3 MB)                                                   
                  8.52 ms   (jitter: 0.60ms, low: 4.94ms, high: 9.62ms)
 Packet Loss:     0.0%
  Result URL: https://www.speedtest.net/result/c/6ab4a55c-bace-43a9-9786-b1871facf941

logger_diginet.py is similar, but differs in that it uses a specific server to test the internet speed (./speedtest -s 31717)
