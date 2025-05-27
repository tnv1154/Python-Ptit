import socket
import hashlib
def client_program():
    host = '127.0.0.1'
    port = 12000
    key = "WrongKey" #Khóa sai

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "Hello, I am Nguyen Viet Thang B22DCAT288 CLIENT"
    hash_message = hashlib.sha512((message + key).encode("utf-16")).hexdigest()

    print(f"Client gui toi Server: {message}")
    client_socket.send(message.encode())
    print(f"Client gui ham bam toi Server: {hash_message}")
    client_socket.send(hash_message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Phan hoi tu Server: {data}")
    client_socket.close()

if __name__ == "__main__":
    client_program()