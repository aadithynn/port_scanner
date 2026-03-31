import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass

def main():
    target = input("Enter target (IP or domain): ")
    print(f"\nScanning target: {target}\n")

    for port in range(1, 1025):  # Common ports
        scan_port(target, port)

    print("\nScan completed.")

if __name__ == "__main__":
    main()