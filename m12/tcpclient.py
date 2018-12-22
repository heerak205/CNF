import socket

def main():
	host = "127.0.0.1"
	port = 5007

	scket = socket.socket()
	scket.connect((host, port))

	message = input("->")
	while message != 'q':
		scket.send(message.encode())
		data1 = scket.recv(1024).decode()
		print("Received from server: " + data1)
		message = input("->")
	socket.close()


if __name__ == '__main__':
	main()