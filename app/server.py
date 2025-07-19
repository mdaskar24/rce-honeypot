import socket
import threading
from app.logger import log_command
from app.webcam import capture_snapshot

HOST = '0.0.0.0'
PORT = 8080

def handle_client(client_socket, address):
    print(f"[+] Connection from {address}")
    client_socket.send(b"Welcome to Secure FTP Server v1.2\nLogin: ")
    client_socket.recv(1024)  # Fake login

    client_socket.send(b"Password: ")
    client_socket.recv(1024)

    client_socket.send(b"Login successful.\n>> ")

    while True:
        try:
            cmd = client_socket.recv(1024).decode('utf-8').strip()
            if not cmd:
                break

            # Log the command
            log_command(address[0], cmd)

            # Suspicious keywords list (expand as needed)
            suspicious_keywords = [
                "upload", "nc", "wget", "curl", "cat /etc/shadow", "passwd", 
                "netstat", "ls -la", "uname", "nmap", "scp", "ftp"
            ]

            # Check for any suspicious activity
            for keyword in suspicious_keywords:
                if keyword in cmd.lower():
                    print(f"[!] Suspicious command detected: {cmd}")
                    capture_snapshot()
                    break

            client_socket.send(b"Command received.\n>> ")
        except Exception as e:
            print(f"[!] Error handling client {address}: {e}")
            break

    client_socket.close()
    print(f"[-] Disconnected {address}")

def start_server():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Honeypot running on {HOST}:{PORT}...")

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
