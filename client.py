import socket
import time
import random

# Configuration
# Change this in client.py
SERVER_IP = '10.207.50.1' # Change this to the server's IP for WiFi testing
PORT = 65432

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            print(f"Connected to server at {SERVER_IP}")
            
            while True:
                # Generate random temperature
                temp = round(random.uniform(20.0, 30.0), 1)
                message = f"Temperature: {temp} C"
                
                # Send data
                s.sendall(message.encode('utf-8'))
                print(f"Sent: {message}")
                
                # Wait 5 seconds
                time.sleep(5)
    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Is it running?")

if __name__ == "__main__":
    start_client()