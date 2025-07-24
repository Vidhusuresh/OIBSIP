import socket
import threading

HOST = '127.0.0.1'  # Change this to server's IP if connecting remotely
PORT = 5000

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[Server] {message}")
        except:
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.sendall(message.encode())
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[+] Connected to server at {HOST}:{PORT}")

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()

    client_socket.close()

if __name__ == "__main__":
    main()
