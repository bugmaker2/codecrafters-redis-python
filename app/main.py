import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client
    while conn.recv(1024):
        conn.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
