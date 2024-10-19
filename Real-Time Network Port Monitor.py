import socket
import time

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

def monitor_ports(host, ports):
    print(f"🚀 Monitoring ports for {host}...")
    status = {}
    for port in ports:
        status[port] = check_port(host, port)

    while True:
        for port in ports:
            is_open = check_port(host, port)
            if is_open != status[port]:
                status[port] = is_open
                state = "OPEN" if is_open else "CLOSED"
                print(f"🔄 Port {port} is now {state}!")
        time.sleep(2)

if __name__ == "__main__":
    target_host = input("🌐 Enter target host (IP): ")
    target_ports = list(map(int, input("💻 Enter ports to monitor (comma-separated): ").split(",")))
    monitor_ports(target_host, target_ports)
