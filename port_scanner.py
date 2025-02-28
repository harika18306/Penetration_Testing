import argparse
import socket
import threading

def port_scanner(target, ports):
    print(f"Scanning {target} on ports {ports}")
    for port in ports:
        threading.Thread(target=scan_port, args=(target, port)).start()

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="module", help="Choose a module")

    # Port Scanner Module
    scanner_parser = subparsers.add_parser("portscan", help="Scan open ports on a target")
    
    # Ask user for target IP interactively
    target_ip = input("Enter target IP or domain: ")
    scanner_parser.add_argument("target", nargs="?", default=target_ip, help="Target IP or domain")
    
    # Ask user for ports interactively
    ports_input = input("Enter ports to scan (comma-separated, e.g., 22,80,443): ")
    ports = list(map(int, ports_input.split(",")))
    scanner_parser.add_argument("ports", nargs="*", type=int, default=ports, help="Ports to scan")

    args = parser.parse_args()

    if args.module == "portscan":
        port_scanner(args.target, args.ports)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()