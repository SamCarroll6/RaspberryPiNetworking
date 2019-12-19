import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

except socket.error as err:
    print("Socket creation error: %s", err)

port = 8081 


#print("Provide target IP: ")
host_ip = input("Provide target IP: ")
print(host_ip)

try:
    s.connect((host_ip, port))
except socket.error as exc:
    print("Error connecting to host:", host_ip, exc)