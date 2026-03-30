import socket

# Function to scan ports
def scan_ports(target_host):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 8080]
    open_ports = []
    closed_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()

    return open_ports, closed_ports

# Main function
if __name__ == '__main__':
    target = input('Enter the target host: ')
    open_ports, closed_ports = scan_ports(target)
    
    print(f'Open ports: {open_ports}')
    print(f'Closed ports: {closed_ports}')