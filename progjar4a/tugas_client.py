from file_client_cli import send_command
import datetime
import threading

def execute_get(id):
    send_command("GET pokijan.jpg")
    print(f"request {id}")

def request_file_pokijan(count=100):
    texec = dict()

    catat_awal = datetime.datetime.now()
    for i in range(0,count):
        print(f"request number {i} of pokijan.jpg")
        texec[i] = threading.Thread(target=execute_get, args=(i))
        texec[i].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for i in range(0, count):
        texec[i].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")

if __name__=='__main__':
    request_file_pokijan()