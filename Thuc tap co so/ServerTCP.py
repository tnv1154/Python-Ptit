import socket

def server_program():
    host = '127.0.0.1'
    port = 12000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()

    data = conn.recv(1024).decode()
    print(f"Nhan tu client {address}: {str(data)}")
    data = "Hello, I am Nguyen Viet Thang B22DCAT288 SERVER"
    print(f"Server phan hoi: {str(data)}")
    conn.send(data.encode())
    conn.close()

if __name__ == "__main__":
    print("Server is running...")
    server_program()


