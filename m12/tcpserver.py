import socket
import csv

def main():
	host = '127.0.0.1'
	port = 5007
	scket = socket.socket()
	scket.bind((host, port))
	scket.listen(3)
	c,addr = scket.accept()
	while True:
		data = c.recv(1024).decode()
		if not data:
			break
		with open('data.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=" ")
			line_count = 0
			file = list(csv_reader)
			#print(file)
			ROLLNUMBER = ['20158501', '20158502', '20158503', '20158504']
			data1 = 'ROLLNUMBER-NOTFOUND'
			if data == ('MARK-ATTENDANCE' + " " + str(ROLLNUMBER)):
				for each in file:
					for i in range(len(ROLLNUMBER)):
						if int(each[0]) != int(ROLLNUMBER[i]):
							print ("sending: " + str(data1))
							c.send(data1.encode())
					 
	conn.close()	

if __name__ == "__main__":
	main()
