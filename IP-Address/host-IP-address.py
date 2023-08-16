import socket

def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except socket.gaierror:
        return None

if __name__ == "__main__":
    host_ip = get_host_ip()
    if host_ip:
        print("Host IP Address:", host_ip)
    else:
        print("Failed to retrieve Host IP Address.")
        
