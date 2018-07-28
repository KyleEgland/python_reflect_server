#! python3
# Client for test the TCP server
import socket


target_host = '127.0.0.1'
target_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((target_host, target_port))

# Send some data
data = 'This is a test'
binary_data = data.encode('utf-8')

client.send(binary_data)

# Receive back some data
response = client.recv(4096)

print(response.decode('utf-8'))
