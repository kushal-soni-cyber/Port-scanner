import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    scan_ports(target, start_port, end_port)
