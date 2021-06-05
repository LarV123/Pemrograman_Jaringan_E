from streamer import stream_file,stream_config
import time
import datetime
from multiprocessing import Process

def stream_all():
    texec = dict()
    configs = stream_config()
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"streaming file {config['filename']} to {config['ip_address']}:{config['port']}")
        waktu = time.time()
        texec[config['filename']] = Process(target=stream_file, args=(config['filename'], config['ip_address'], config['port']))
        texec[config['filename']].start()
    for config in configs:
        texec[config['filename']].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    
if __name__=='__main__':
    stream_all()