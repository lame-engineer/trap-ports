import socket

target = "127.0.0.1"

def scanport(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

for port1 in range (1, 50000):
    rs = scanport(port1)
    if rs:
        print(f"port {port1} is open")
