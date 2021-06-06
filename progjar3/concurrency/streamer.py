import socket

CHUNK_SIZE = 1024

def stream_config():
    return [{'ip_address':'192.168.122.151', 'filename':'cicero.txt', 'port':5005},
    {'ip_address':'192.168.122.217', 'filename':'english.txt', 'port':5005},
    {'ip_address':'192.168.122.111', 'filename':'lorep.txt', 'port':5005},
    {'ip_address':'192.168.122.186', 'filename':'pangram.txt', 'port':5005},
    {'ip_address':'192.168.122.97', 'filename':'random.txt', 'port':5005},]

def stream_file(filename, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    file = open(filename, "r")
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        sock.sendto(chunk.encode(), (ip, port))
    
if __name__ == '__main__' :
    configs = stream_config()
    for config in configs:
        print(f"streaming file {config['filename']} to {config['ip_address']}:{config['port']}")
