from streamer import stream_file,stream_config
import time
import datetime
import concurrent.futures

def stream_all():
    texec = dict()
    configs = stream_config()
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"streaming file {config['filename']} to {config['ip_address']}:{config['port']}")
        texec[config['filename']] = task.submit(stream_file, config['filename'], config['ip_address'], config['port'])
    for config in configs:
        status_task[config['filename']]=texec[config['filename']].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

if __name__=='__main__':
    stream_all()