import socket


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, addr = server_socket.accept()
    with connection:
        print(f"Connected by {addr}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(b"+PONG\r\n")
        connection.close()

if __name__ == "__main__":
    main()
