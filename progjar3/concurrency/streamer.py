import socket

CHUNK_SIZE = 1024

def stream_config():
    return [{'ip_address':'127.0.0.1', 'filename':'cicero.txt', 'port':5005},
    {'ip_address':'127.0.0.1', 'filename':'english.txt', 'port':5005},
    {'ip_address':'127.0.0.1', 'filename':'lorep.txt', 'port':5005},
    {'ip_address':'127.0.0.1', 'filename':'pangram.txt', 'port':5005},
    {'ip_address':'127.0.0.1', 'filename':'random.txt', 'port':5005},]

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