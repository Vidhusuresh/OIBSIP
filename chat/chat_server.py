import socket
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 5000         # Non-privileged port

def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"['client'] {message}")
        except:
            break
    conn.close()
    print(f"[-] Disconnected from {addr}")

def send_messages(conn):
    while True:
        try:
            message = input()
            conn.sendall(message.encode())
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Server listening on {HOST}:{PORT}...")

    conn, addr = server.accept()

    recv_thread = threading.Thread(target=handle_client, args=(conn, addr))
    send_thread = threading.Thread(target=send_messages, args=(conn,))
    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()

    server.close()

if __name__ == "__main__":
    main()
