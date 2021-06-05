from streamer import stream_file,stream_config
import time
import datetime
from multiprocessing import Process, Pool

def stream_all():
    texec = dict()
    configs = stream_config()
    status_task = dict()
    task_pool = Pool(processes=20)
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"streaming file {config['filename']} to {config['ip_address']}:{config['port']}")
        texec[config['filename']] = task_pool.apply_async(func=stream_file, args=(config['filename'], config['ip_address'], config['port']))
    for config in configs:
        status_task[config['filename']]=texec[config['filename']].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

if __name__=='__main__':
    stream_all()