import socket
import argparse

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")

    args = parser.parse_args()

    print(f"\nScanning {args.target} from port {args.start} to {args.end}\n")

    for port in range(args.start, args.end + 1):
        scan_port(args.target, port)

    print("\nScan completed.")

if __name__ == "__main__":
    main()
