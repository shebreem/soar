import socket
import time

def get_ip_address(website):
    try:
        hostname = socket.gethostbyname(website)
        return hostname
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

while True:
    ip_address = get_ip_address(input("web: "))
    if ip_address:
        print(f"IP Address: {ip_address}")
    else:
        print("Failed to get IP Address.")
    time.sleep(2) # Wait for 5 seconds before fetching again
