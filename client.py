import socket

host = "127.0.0.1"
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("[*] Connected to honeypot")

while True:
    cmd = input(">> ")
    if cmd.lower() in ["exit", "quit"]:
        break
    client.send(cmd.encode())
    response = client.recv(4096).decode()
    print(response)
