import socket

# Ask user for target IP
target = input("Enter Target IP: ")

# Port range (e.g., 1 to 100)
start_port = 1
end_port = 100

print(f"\n[+] Scanning ports {start_port} to {end_port} on {target}\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # 0.5 sec timeout for faster scan
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()
