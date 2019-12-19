import socket

s = socket.socket()
print("Socket created")

port = 8081

s.bind(('', port))
print("Socket bound")

s.listen(5)
print("Socket is listening")

while True:
	
	c, addr = s.accept()
	print('Connection received from', addr)

	tosend = "Message received, thank you."

	c.send(tosend.encode())

	c.close()

