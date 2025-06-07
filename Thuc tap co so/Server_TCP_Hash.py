import socket
import hashlib
def server_program():
    host = '127.0.0.1'
    port = 12000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()

    key = "NguyenVietThang_B22DCAT288"
    data = conn.recv(1024).decode()
    data_hash = conn.recv(1024).decode()
    print(f"Nhan tu Client: {data}")
    print(f"Nhan ham bam SHA-512 cua thong diep tren tu Cient: {data_hash}")
    sv_hash = hashlib.sha512((data + key).encode("utf-16")).hexdigest()
    data_s = "Ma hoa thanh cong! \nHello, I am Nguyen Viet Thang B22DCAT288 SERVER"
    print(f"Server phan hoi: {data_s}")
    print(f"Server bam thong diep thanh: {sv_hash}")
    if data_hash != sv_hash:
        data_s = "The received message has lost its integrity"
    conn.send(data_s.encode())
    conn.close()

if __name__ == "__main__":
    print("Server is running...")
    server_program()

