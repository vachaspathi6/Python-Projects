import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")
    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)
        message = client_socket.recv(1024)
        print("Received message:", message.decode())
        client_socket.close()

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    message = input("Enter message: ")
    client_socket.send(message.encode())
    client_socket.close()

def main():
    print("1. Start Server")
    print("2. Start Client")
    choice = input("Enter your choice: ")
    if choice == '1':
        server()
    elif choice == '2':
        client()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
