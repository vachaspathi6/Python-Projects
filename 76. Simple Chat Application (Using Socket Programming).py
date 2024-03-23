import socket

def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on port:", port)

    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print("Client:", message)
        reply = input("Server: ")
        conn.send(reply.encode())

    conn.close()
    server_socket.close()

def client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == 'bye':
            break
        reply = client_socket.recv(1024).decode()
        print("Server:", reply)

    client_socket.close()

def main():
    role = input("Enter your role (server/client): ")
    if role.lower() == 'server':
        server()
    elif role.lower() == 'client':
        client()
    else:
        print("Invalid role")

if __name__ == "__main__":
    main()
