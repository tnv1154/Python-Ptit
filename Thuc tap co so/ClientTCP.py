
import socket

def client_program():
    host = '127.0.0.1'
    port = 12000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "Hello, I am Nguyen Viet Thang B22DCAT288 CLIENT"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Phan hoi tu Server: {data}")
    client_socket.close()

if __name__ == "__main__":
    client_program()