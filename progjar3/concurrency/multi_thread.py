from streamer import stream_file,stream_config
import datetime
import threading

def stream_all():
    texec = dict()
    configs = stream_config()

    catat_awal = datetime.datetime.now()

    for config in configs:
        print(f"streaming file {config['filename']} to {config['ip_address']}:{config['port']}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[config['filename']] = threading.Thread(target=stream_file, args=(config['filename'], config['ip_address'], config['port']))
        texec[config['filename']].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for config in configs:
        texec[config['filename']].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    stream_all()